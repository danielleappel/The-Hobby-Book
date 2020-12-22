# Create the data structure for the hobby book
NUM_PHOTOS = 6
NUM_PROJS = 6
NUM_HOBBIES = 6

def list_str(lis):
    """Return a string containing the input list with commas seperating"""
    as_str = ""
    for item in lis:
        as_str += " " + str(item) + ","
    return as_str[:-1]

def list_str_breaks(lis):
    """Return a string containing the input list with line breaks seperating"""
    as_str = ""
    for item in lis:
        as_str += str(item) + "\n"
    return as_str[:-1]

class Hobby_Book:
    
    def __init__(self):
        """Construct the book """
        self.__hobbies = [None] * NUM_HOBBIES

    def add_hobby(self, hobby, i):
        """Add a hobby to the book"""
        self.__hobbies[i] = hobby

    def update_hobby_name(self, curr_hobby, new_name):
        """Update the hobby name of a given hobby"""
        for hobby in self.__hobbies:
            if hobby == curr_hobby:
                hobby.update_name(new_name)

    def update_hobby_cover_photo(self, curr_hobby, new_cover_photo):
        """Update the cover photo of a given hobby"""
        for hobby in self.__hobbies:
            if hobby == curr_hobby:
                hobby.update_cover_photo(new_cover_photo)

    def add_project_to_hobby(self, curr_hobby, proj, i):
        for hobby in self.__hobbies:
            if hobby == curr_hobby:
                hobby.add_project(proj, i)

    def update_project_name(self, hobby_curr, proj, project_name):
        for hobby in self.__hobbies:
            if hobby == hobby_curr:
                hobby.update_project_name(proj, project_name)

    def update_project_cover_photo(self, hobby_curr, proj, photo):
        for hobby in self.__hobbies:
            if hobby == hobby_curr:
                hobby.update_project_cover_photo(proj, photo)

    def add_project_photo(self, hobby_curr, proj, photo, i):
        for hobby in self.__hobbies:
            if hobby == hobby_curr:
                hobby.add_project_photo(proj, photo, i)

    def add_project_link(self, hobby_curr, proj, link):
        for hobby in self.__hobbies:
            if hobby == hobby_curr:
                hobby.add_project_link(proj, link)

    def add_project_note(self, hobby_curr, proj, note):
        for hobby in self.__hobbies:
            if hobby == hobby_curr:
                hobby.add_project_note(proj, note)

    def __str__(self):
        """Create a string of the application"""
        return list_str_breaks(self.__hobbies)

    def get_hobby(self, i):
        return self.__hobbies[i]

class Hobby:
    
    def __init__(self, name, cover_photo):
        """Construct a hobby out of a name and cover photo"""
        self.__name = name
        self.__cover_photo = cover_photo
        self.__projects = [None] * NUM_PROJS

    def update_name(self, new_name):
        """Update the name of the hobby"""
        self.__name = new_name

    def update_cover_photo(self, new_cover_photo):
        """Update the cover photo of the hobby"""
        self.__cover_photo = new_cover_photo

    def add_project(self, proj, i):
        """Add a project to the list of projects"""
        self.__projects[i] = proj

    def update_project_name(self, curr_proj, proj_new_name):
        """Update the name of a specified project"""
        for proj in self.__projects:
            if proj == curr_proj:  # Find the project with the same current name
                proj.update_name(proj_new_name)      # Update the project's name

    def update_project_cover_photo(self, proj_curr, new_cover_photo):
        """Update the cover photo of a specified project"""
        for proj in self.__projects:
            if proj == proj_curr:            # Find the project with the same name
                proj.update_cover_photo(new_cover_photo)  # Update the project's cover photo
    
    def add_project_photo(self, proj_curr, photo, i):
        """Add a photo to the specified project"""
        for proj in self.__projects:
            if proj == proj_curr:  # Find the project with the same name
                proj.add_photo(photo, i)           # Add the photo

    def add_project_link(self, proj_curr, link):
        """Add a link to the specified project"""
        for proj in self.__projects:
            if proj == proj_curr:  # Find the project with the same name
                proj.update_links(link)             # Add the photo

    def add_project_note(self, proj_curr, note):
        """Add a note to the specified project"""
        for proj in self.__projects:
            if proj == proj_curr:  # Find the project with the same name
                proj.update_note(note)             # Add the photo

    def __eq__(self, other):
        """Test if two hobbies are equal"""
        return self.__name == other.__name

    def __str__(self):
        """Create a string of the project"""
        hobby_string = "Hobby Name: " + self.__name
        hobby_string += "\n   Cover Photo: " +  self.__cover_photo
        hobby_string += "\n   Projects: \n" +  list_str_breaks(self.__projects)

        return hobby_string

    def get_name(self):
        """Function to return the name

            Only used to display in the GUI
        """
        return self.__name

    def get_cover_photo(self):
        """Function to return the cover photo

            Only used to display in the GUI
        """
        return self.__cover_photo   

    def get_project(self, i):
        """Function to return the photo at index i

            Only used to display in the GUI
        """
        return self.__projects[i]

class Project:

    def __init__(self, name, cover_photo):
        """Construct a project out of a name and cover photo"""
        self.__name = name
        self.__cover_photo = cover_photo

        self.__links = ""
        self.__note = ""
        self.__dates = ""

        self.__photos = [None] * NUM_PHOTOS
        
    def add_date(self, new_date):
        """Add a date to the project"""
        if self.__dates == "":
            self.__dates = new_date
        else:
            self.__dates += ", " + new_date   

    def update_name(self, new_name):
        """Update the name of a project"""
        self.__name = new_name

    def update_cover_photo(self, new_cover_photo):
        """Update the cover photo of a project"""
        self.__cover_photo = new_cover_photo

    def update_links(self, new_link):
        """Add a link to the project"""
        self.__links = new_link

    def update_note(self, new_note):
        """Add a note to the project"""
        self.__note = new_note

    def add_photo(self, new_photo, i):
        """Add a photo to the project"""
        self.__photos[i] = new_photo

    def __eq__(self, other):
        """Test if two projects are equal"""
        return self.__name == other.__name

    def __str__(self):
        """Create a string of the project"""
        proj_string = "   Project Name: " + self.__name
        proj_string += "\n      Cover Photo: " +  self.__cover_photo
        proj_string += "\n      Links: " +  self.__links
        proj_string +=   "      Note: " +  self.__note
        proj_string +=   "      Photos: " +  list_str(self.__photos)

        return  proj_string

    def get_name(self):
        """Function to return the name

            Only used to display in the GUI
        """
        return self.__name

    def get_dates(self):
        """Function to return the dates worked on

            Only used to display in the GUI
        """
        return self.__dates

    def get_cover_photo(self):
        """Function to return the cover photo

            Only used to display in the GUI
        """
        return self.__cover_photo

    def get_note(self):
        """Function to return the notes

            Only used to display in the GUI
        """
        return self.__note  

    def get_links(self):
        """Function to return the cover photo

            Only used to display in the GUI
        """
        return self.__links

    def get_photo(self, i):
        """Function to return the cover photo

            Only used to display in the GUI
        """
        return self.__photos[i]