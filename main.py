from controller import Controller


"""Project structure:
Main
- One main file that creates the controller

Controller
- Creates an instance of view
- Creates an instance of model = Flashcards()


View
- The view is the app instance
- Main app instance imports all files

Model
- data.csv
- flashcards (Needs to keep track of last all answers on each card)
- card

Documentation readme-file:
- Project structure
- Descriptions of each file and object
- Purpose of the project
- Learning goals of the project

Test (own folder with test files and test_data.csv-file)
- txt-file explaining the testing process.
- Unit tests
- test a lot of different user stories

"""

# PROJECT DEFECTS FOUND
# TODO: Cannot add new user properly
# TODO: Change text to no spaces i username
# TODO: Edit user/edit card should keep original text in textbox.
# TODO: Reverse backup list. Newest first
# TODO: Update all docstrings


if __name__ == "__main__":
    c = Controller()
