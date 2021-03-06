# The-Hobby-Book
A Python application using a Graphical User Interface (GUI) to help organize resources for your hobbies

My overarching goal with this project was to create an interactive application that allows people to store resources for their hobbies and projects. 
For instance, if you love to cook, you can store pictures of your food, recipes, links to recipes, notes, and dates you worked on each recipe. 
If you love to knit, you can store photos of your completed work and patterns, links to patterns, notes specific to each knitting project, and the dates you worked on it. 

Additionally, there is a normal calculator and a unit conversion calculator available.

- The *Hobby Book* stores *Hobbies*.
- *Hobbies* store a name, cover photo, and list of *Projects*.
- *Projects* store a name, cover photo, notes, links, dates, and photos.

To run my code, the files needed are:

-	hobby_book_structure.py
-	hobby_book.py
-	project.py
-	hobby.py
-   hobby_calculator.py

Before running, first install PySimpleGUI with the command

    pip install PySimpleGUI
or check [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) for more info. Then simply run the code in [hobby_book.py](https://github.com/danielleappel/The-Hobby-Book/blob/main/hobby_book.py) which will launch the GUI. 

My approach to building my project was to first create the actual object-oriented structure in [hobby_book_structure.py](https://github.com/danielleappel/The-Hobby-Book/blob/main/hobby_book_structure.py). 
It stores the file paths, notes, names, dates, projects, etc. It is fairly straightforward because most of the error checking for inputs happens within the Hobby Book. 
Then I built the GUI for the Projects in the file [project.py](https://github.com/danielleappel/The-Hobby-Book/blob/main/project.py) file. After that I built GUI for Hobbies. 
Finally, I built the overall Hobby Book GUI. This is the most complicated and calls the Project and Hobby GUIs as well. 

Here are a few shots of what my Hobby Book looks like in action. First, here’s a look at the overall Hobby Book 
![Hobby Book](https://github.com/danielleappel/The-Hobby-Book/blob/main/Images/Hobby_Book_View.png)
 
And here’s a view of a Project,
![Project](https://github.com/danielleappel/The-Hobby-Book/blob/main/Images/Project_View.png)
 
And here’s a look at the unit conversion calculator!
![Unit Conversion Calculator](https://github.com/danielleappel/The-Hobby-Book/blob/main/Images/Unit_Conversion_Calculator.png) 
