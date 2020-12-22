# Create hobbies

import PySimpleGUI as sg  
import os.path    

import hobby_book_structure as hbs

sg.ChangeLookAndFeel('Reddit')      

def create_hobby():
    """GUI Hobby Creator
    
       Add the name and cover photo in this interactive GUI
    """
    # ------ Setting up columns --------------
    file_list_column = [
        [
            sg.Text("Cover photo  "),
            sg.In(size=(63, 2), enable_events=True, key="-FILE-"),
            sg.FileBrowse(tooltip="Select a cover photo for your Hobby (.png or .gif only)")
        ]
    ]

    input_name_column = [
        [
            sg.Text('Hobby Name'), 
            sg.InputText(size=(72,1), key = "-NAME-", enable_events=True),
        ]
    ]

    image_viewer_column = [
        [sg.Text(size=(43, 2), key="-FILE_NAME-")],
        [sg.Image(key="-IMAGE-")]
    ]      

    # ------ Layout ---------------- #
    layout = [      
        [sg.Text('Create a new Hobby', font=("Helvetica", 25))], 
        [sg.Text('Please enter your Hobby Name and Cover Photo.')],
        [sg.Frame('Select a name', [[
            sg.Column(input_name_column),
            sg.VSeperator(),
            sg.Text(size=(15,2), key='-NAME_OUT-', font='Helvetica 31', text_color='purple', pad=(1,1))
            ]])],              
        [sg.Frame('Select a Cover Photo', [[
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column) ]])],   
        [sg.Submit(tooltip='Click Submit to create your Hobby'), sg.Cancel(tooltip='Click here to cancel')]    
    ]      

    # ------- Create the Hobby window --------
    window = sg.Window('Create a Hobby', layout, grab_anywhere=False)      
    submitted = False

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        # Submit => create the hobby and go to the next screen
        if event == "Submit": 
            name = values["-NAME-"]
            cover_photo = values["-FILE-"]
            hobby = hbs.Hobby(name, cover_photo) 
            submitted = True
            break 
        if event == "-FILE-":
            file = values["-FILE-"]
            if file.lower().endswith((".png",".gif")):
                window["-FILE_NAME-"].update(os.path.basename(file))
                window["-IMAGE-"].update(file, size=(250,250))
        if event == "-NAME-":
            name = values["-NAME-"]
            window["-NAME_OUT-"].update(name)

    window.close()
    return hobby