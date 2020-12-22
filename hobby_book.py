# Create and launch the interactive hobby book

import PySimpleGUI as sg  
import os.path    

import hobby_book_structure as hbs
import hobby as hb
import project as pj

sg.ChangeLookAndFeel('Reddit')  

NUM_HOBBIES = 6
NUM_PROJECTS = 6

# Define default width and height for images (in pixels)
H = 300 
W = 400
# Define default width and height for projects (in pixels)
P_H = 250
P_W = 300

def launch_hobby_book():
    # ------- Create the hobby book object -------
    hobby_book = hbs.Hobby_Book()
    
    # ------- Set up columns/sub-layouts ---------
    title_column = [
        [sg.Text("The Hobby Book", size=(30,1), font='Helvetica 32', justification="center", text_color='purple')]
    ]

    # Create name lists to index the elements on the page 
    hobbies = ["Hobby0", "Hobby1", "Hobby2", "Hobby3", "Hobby4", "Hobby5"]
    hobby_names = ["-HOBBY0-", "-HOBBY1-", "-HOBBY2-", "-HOBBY3-", "-HOBBY4-", "-HOBBY5-"]
    hobby_cover_photos = ["-HOBBY0_COVER_PHOTO-", "-HOBBY1_COVER_PHOTO-", "-HOBBY2_COVER_PHOTO-", "-HOBBY3_COVER_PHOTO-", "-HOBBY4_COVER_PHOTO-", "-HOBBY5_COVER_PHOTO-"]

    create_hobby_list = ["-CREATE_HOBBY0-", "-CREATE_HOBBY1-", "-CREATE_HOBBY2-", "-CREATE_HOBBY3-", "-CREATE_HOBBY4-", "-CREATE_HOBBY5-"]
    view_hobby_list = ["-VIEW_HOBBY0-", "-VIEW_HOBBY1-", "-VIEW_HOBBY2-", "-VIEW_HOBBY3-", "-VIEW_HOBBY4-", "-VIEW_HOBBY5-"]
    
    hobby0_layout = hobby1_layout = hobby2_layout = hobby3_layout = hobby4_layout = hobby5_layout = [[]]
    hobby_layout = [hobby0_layout, hobby1_layout, hobby2_layout, hobby3_layout, hobby4_layout, hobby5_layout]

    for i in range(0, NUM_HOBBIES):
        hobby_layout[i] = [
            [sg.Text(size=(20,1), key=hobby_names[i], font='Helvetica 20', text_color='purple')],
            [sg.Image(size=(W,H), key=hobby_cover_photos[i])], 
            [sg.Button("New", tooltip="Create a new Hobby", enable_events=True, key=create_hobby_list[i]),
                sg.Button("View", tooltip="Click to view and edit your Hobby", enable_events=True, key=view_hobby_list[i])]    
        ]

    create_project_list = ["-CREATE_PROJ0-", "-CREATE_PROJ1-", "-CREATE_PROJ2-", "-CREATE_PROJ3-", "-CREATE_PROJ4-", "-CREATE_PROJ5-"]
    view_project_list = ["-VIEW_PROJ0-", "-VIEW_PROJ1-", "-VIEW_PROJ2-", "-VIEW_PROJ3-", "-VIEW_PROJ4-", "-VIEW_PROJ5-"]
    
    project_names = ["-PROJ0_NAME-", "-PROJ1_NAME-", "-PROJ2_NAME-", "-PROJ3_NAME-", "-PROJ4_NAME-", "-PROJ5_NAME-"]
    project_cover_photos = ["-PROJ0_COVER_PHOTO-", "-PROJ1_COVER_PHOTO-", "-PROJ2_COVER_PHOTO-", "-PROJ3_COVER_PHOTO-", "-PROJ4_COVER_PHOTO-", "-PROJ5_COVER_PHOTO-"]
    projects = ["Proj0", "Proj1", "Proj2", "Proj3", "Proj4", "Proj5"]

    project_notes_list = ["-PROJ0_NOTES-", "-PROJ1_NOTES-", "-PROJ2_NOTES-", "-PROJ3_NOTES-", "-PROJ4_NOTES-", "-PROJ5_NOTES-"]

    proj0_layout = proj1_layout = proj2_layout = proj3_layout = proj4_layout = proj5_layout = None
    proj_layout = [proj0_layout, proj1_layout, proj2_layout, proj3_layout, proj4_layout, proj5_layout]

    for i in range(0, NUM_PROJECTS):
        proj_layout[i] = [
            [sg.Text(size=(20,1), key=project_names[i], font='Helvetica 15', text_color='purple')],
            [sg.Image(size=(P_W,P_H), key=project_cover_photos[i])],
            [sg.Text(size=(30,3), key=project_notes_list[i], font='Helvetica 11')],
            [sg.Button("New", tooltip="Create a new Project", enable_events=True, key=create_project_list[i]),
                sg.Button("View", tooltip="Click to view and edit your Project", enable_events=True, key=view_project_list[i])]
        ]
    active_hobby_column = [
        [sg.Text(size=(20,1), key="-ACTIVE_HOBBY-", font='Helvetica 20', text_color='purple', justification='center')]
    ]
    active_hobby = None

    # ------ Layout ---------------- #
    layout = [      
        [sg.Column(title_column)],
        [sg.Column(active_hobby_column, justification='right')],
        [sg.TabGroup([[sg.Tab(hobbies[i], hobby_layout[i]) for i in range(0, NUM_HOBBIES)]]),
            sg.TabGroup([[sg.Tab(projects[i], proj_layout[i]) for i in range(0, NUM_PROJECTS)]])],
        [sg.CloseButton("Close", tooltip="Click here to close the window")]
    ]

    # ------- Launch the hobby book window --------
    window = sg.Window('The Hobby Book', layout, grab_anywhere=True)

    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            break
        if event in create_hobby_list:
            # If the user is adding a hobby
            i = (0 if event == "-CREATE_HOBBY0-" else
                         1 if event == "-CREATE_HOBBY1-" else
                         2 if event == "-CREATE_HOBBY2-" else
                         3 if event == "-CREATE_HOBBY3-" else
                         4 if event == "-CREATE_HOBBY4-" else
                         5)
            try:
                new_hobby = hb.create_hobby()
                hobby_book.add_hobby(new_hobby, i)

                window[hobby_names[i]].update(new_hobby.get_name())
                window[hobby_cover_photos[i]].update(new_hobby.get_cover_photo(), size=(W,H))
            except:
                # Do nothing if the user ends the hobby constructor without submitting
                pass
        if event in view_hobby_list:
            # First set the active hobby
            i = (0 if event == "-VIEW_HOBBY0-" else
                 1 if event == "-VIEW_HOBBY1-" else
                 2 if event == "-VIEW_HOBBY2-" else
                 3 if event == "-VIEW_HOBBY3-" else
                 4 if event == "-VIEW_HOBBY4-" else
                 5)
            # Try to load the active hobby
            try:
                window["-ACTIVE_HOBBY-"].update(hobby_book.get_hobby(i).get_name())
                active_hobby = i
                hob = hobby_book.get_hobby(i)
                
                # Now load each project
                for i in range(0, NUM_PROJECTS):
                    proj = hob.get_project(i)
                    try:
                        window[project_names[i]].update(proj.get_name())
                        window[project_cover_photos[i]].update(proj.get_cover_photo(), size=(P_W,P_H))
                        window[project_notes_list[i]].update(proj.get_note())
                    except:
                        window[project_names[i]].update("")
                        window[project_cover_photos[i]].update()
                        window[project_notes_list[i]].update("")
            except:
                sg.popup("Please create a Hobby first")
        if event in create_project_list:
            if active_hobby == None:
                sg.popup('Please select a Hobby first')
            else:
                i = (0 if event == "-CREATE_PROJ0-" else
                         1 if event == "-CREATE_PROJ1-" else
                         2 if event == "-CREATE_PROJ2-" else
                         3 if event == "-CREATE_PROJ3-" else
                         4 if event == "-CREATE_PROJ4-" else
                         5)
                try:
                    hobby = hobby_book.get_hobby(active_hobby)
                    new_proj = pj.create_project()

                    hobby.add_project(new_proj, i)

                    window[project_names[i]].update(new_proj.get_name())
                    window[project_cover_photos[i]].update(new_proj.get_cover_photo(), size=(P_W,P_H))
                    window[project_notes_list[i]].update(new_proj.get_note())
                    print(new_proj.get_note())
                except:
                    # Do nothing if the user ends the project constructor without submitting
                    pass
        if event in view_project_list:
            if active_hobby == None:
                sg.popup('Please select a Hobby first')
            else:
                i = (0 if event == "-VIEW_PROJ0-" else
                         1 if event == "-VIEW_PROJ1-" else
                         2 if event == "-VIEW_PROJ2-" else
                         3 if event == "-VIEW_PROJ3-" else
                         4 if event == "-VIEW_PROJ4-" else
                         5)
                hobby = hobby_book.get_hobby(active_hobby)
                proj = hobby.get_project(i)
                try:
                    new_proj = pj.edit_project(proj)
                except:
                    # If the user doesn't input a project, just create a blank one
                    new_proj = pj.edit_project(hbs.Project("",""))

                # Update the screen after editing
                window[project_names[i]].update(new_proj.get_name())
                window[project_cover_photos[i]].update(new_proj.get_cover_photo(), size=(P_W,P_H))
                window[project_notes_list[i]].update(new_proj.get_note())

    window.close()

if True:
    launch_hobby_book()