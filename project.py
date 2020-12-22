# Create projects and edit them

import PySimpleGUI as sg  
import os.path    

import hobby_book_structure as hbs

sg.ChangeLookAndFeel('Reddit')  

# Define default width and height for images (in pixels)
H = 300 
W = 400
NUM_PHOTOS = 6

def create_project():
    """GUI Project Creator
    
       Add the name and cover photo in this interactive GUI
    """
    # ------ Setting up columns --------------
    file_list_column = [
        [
            sg.Text("Cover photo  "),
            sg.In(size=(63, 2), enable_events=True, key="-FILE-"),
            sg.FileBrowse(tooltip="Select a Cover Photo for your Project (.png or .gif only)")
        ]
    ]

    input_name_column = [
        [
            sg.Text('Project Name'), 
            sg.InputText(size=(72,1), key = "-NAME-", enable_events=True),
        ]
    ]

    image_viewer_column = [
        [sg.Text(size=(42, 2), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")]
    ]      

    # ------ Layout ---------------- #
    layout = [      
        [sg.Text('Create a new Project', font=("Helvetica", 25))], 
        [sg.Text('Please enter your Project Name and Cover Photo.')],
        [sg.Frame('Select a name', [[
            sg.Column(input_name_column),
            sg.VSeperator(),
            sg.Text(size=(15,2), key='-NAME_OUT-', font='Helvetica 31', text_color='purple', pad = (1,1))
            ]])],              
        [sg.Frame('Select a Cover Photo', [[
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column) ]])],   
        [sg.Submit(tooltip='Click Submit to create your Project'), sg.Cancel(tooltip='Click here to cancel')]    
    ]      

    # ------- Create the project window --------
    window = sg.Window('Create a Project', layout, default_element_size=(40, 1), grab_anywhere=True)      

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break
        # Submit => create the project and go to the next screen
        if event == "Submit": 
            name = values["-NAME-"]
            cover_photo = values["-FILE-"]
            proj = hbs.Project(name, cover_photo) 

            window.close()
            
            edit_project(proj) 
            return proj
        if event == "-FILE-":
            file = values["-FILE-"]
            if file.lower().endswith((".png",".gif")):
                window["-TOUT-"].update(os.path.basename(file))
                window["-IMAGE-"].update(file, size=(250,250))
        if event == "-NAME-":
            name = values["-NAME-"]
            window["-NAME_OUT-"].update(name)

def edit_project(proj):
    """GUI Project Editor
    
       Edit any input Project in this interactive GUI
    """

    # ------- Set up columns/sub-layouts ---------
    proj_name_column = [
        [sg.Text(proj.get_name(), size=(36,1), font='Helvetica 32', justification="center", text_color='purple', key="-PROJ_NAME-")],
        [sg.In(size=(58,1), enable_events=True, key="-NEW_NAME-"),
            sg.Button('Save', key = "-SAVE_NAME-", tooltip="Click here change the Project name")
        ] 
    ]   

    note_column = [
        [sg.Text("Project note")],
        [sg.Multiline(proj.get_note(), size=(54, 19), key="-NOTE-", enable_events=True)],
    ]

    links_column = [
        [sg.Text("Project links")],
        [sg.Multiline(proj.get_links(), size=(54, 19), key="-LINKS-", enable_events=True)]
    ]

    dates_column = [
        [sg.Text("Select the dates you have worked on this Project")],
        [sg.CalendarButton("Calendar", tooltip="Select the dates of your Project", enable_events=True, key="-CALENDAR_DATE-")],
        [sg.Text(proj.get_dates(), key="-OUTPUT_DATES-", size=(54,18))]
    ]

    cover_photo_layout = [
        [sg.Image(proj.get_cover_photo(), key="-COVER_PHOTO-", size=(W,H))],
        [sg.In(size=(56, 1), enable_events=True, key="-UPDATE_COVER_PHOTO-"),
            sg.FileBrowse(tooltip="Click here to select a new Cover Photo (.png or .gif only)")]
    ] 

    # Declare the layout variables
    photo_names = ["-PHOTO0-", "-PHOTO1-", "-PHOTO2-", "-PHOTO3-", "-PHOTO4-", "-PHOTO5-"]
    photo_files = ["-PHOTO0_FILE-", "-PHOTO1_FILE-", "-PHOTO2_FILE-", "-PHOTO3_FILE-", "-PHOTO4_FILE-", "-PHOTO5_FILE-"]
    photos = ["Photo0", "Photo1", "Photo2", "Photo3", "Photo4", "Photo5"]
    
    photo0_layout = photo1_layout = photo2_layout = photo3_layout = photo4_layout = photo5_layout = [[]]
    photo_layout = [cover_photo_layout, photo0_layout, photo1_layout, photo2_layout, photo3_layout, photo4_layout, photo5_layout]

    photo_tab_list = ["-COVER_PHOTO_TAB-", "-PHOTO0_TAB-", "-PHOTO1_TAB-", "-PHOTO2_TAB-", "-PHOTO3_TAB-", "-PHOTO4_TAB-", "-PHOTO5_TAB-"]
    tab_name = ['Cover Photo', 'Photo0',  'Photo1',  'Photo2',  'Photo3',  'Photo4',  'Photo5']

    for i in range(1, NUM_PHOTOS+1):
        # Create the layout for entered photos + get the tab names
        photo = proj.get_photo(i-1)
        if not photo == None:
            tab_name[i] = os.path.basename(photo)[:-4]

        photo_layout[i] = [
            [sg.Image(photo, key=photo_names[i-1], size=(W,H))], 
            [sg.In(size=(56, 1), enable_events=True, key=photo_files[i-1]),
                sg.FileBrowse(tooltip="Select a photo for your Project (.png or .gif only)")]
        ]

    # ------ Layout ---------------- #
    layout = [      
        [sg.Column(proj_name_column)],
        [sg.TabGroup([[sg.Tab(tab_name[i], photo_layout[i], key=photo_tab_list[i]) for i in range(NUM_PHOTOS+1)]]),
            sg.VSeparator(),
            sg.TabGroup([[sg.Tab('Notes', note_column), 
                sg.Tab('Links', links_column),
                sg.Tab('Dates', dates_column)]]),
        ],
        [sg.Button("Submit", key='-SUBMIT-', tooltip="Click here to submit the window")]
    ]      

    # ------- Launch the project editor window --------
    window = sg.Window('Edit your Project', layout, grab_anywhere=True)      

    while True:
        event, values = window.read()
        if event == "-SUBMIT-" or event == sg.WIN_CLOSED:
            # First save the notes
            new_note = values["-NOTE-"]
            proj.update_note(new_note)

            # Now save the linsk
            new_links = values["-LINKS-"]
            proj.update_links(new_links)
            break
        if event == "-SAVE_NAME-":
            new_name = values["-NEW_NAME-"]
            proj.update_name(new_name)
            window["-PROJ_NAME-"].update(new_name)
        if event == "-UPDATE_COVER_PHOTO-":
            new_cover_photo = values["-UPDATE_COVER_PHOTO-"]
            # Verify the selected file is a .png or .gif
            if new_cover_photo.lower().endswith((".png",".gif")):
                window["-COVER_PHOTO-"].update(new_cover_photo, size=(W,H))
                proj.update_cover_photo(new_cover_photo)
        if event == "-NEW_NAME-":
            # If they are typing a new name, update the large name
            new_name = values["-NEW_NAME-"]
            window["-PROJ_NAME-"].update(new_name)
        if event in photo_files:
            # If the user is adding a photo
            i = (0 if event == "-PHOTO0_FILE-" else
                         1 if event == "-PHOTO1_FILE-" else
                         2 if event == "-PHOTO2_FILE-" else
                         3 if event == "-PHOTO3_FILE-" else
                         4 if event == "-PHOTO4_FILE-" else
                         5)
            photo_file = values[event]
            if photo_file.lower().endswith((".png",".gif")):
                window[photo_names[i]].update(photo_file, size=(W,H))
                proj.add_photo(photo_file, i)
                window[photo_tab_list[i]].update(os.path.basename(photo_file)[:-4])
        if event == "-CALENDAR_DATE-":
            new_date = values[event][:-8]
            proj.add_date(new_date)

            window["-OUTPUT_DATES-"].update(proj.get_dates())

    window.close()
    return proj