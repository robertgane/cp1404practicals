"""
CP1404/CP5632 Practical - Project Management Program.
"""
from prac_07.project import Project

FILENAME = "../prac_07/projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- " \
       "(A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Displays project_management program."""
    projects = []
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            load_file(FILENAME, projects)
        elif menu_choice == "S":
            save_project()
        elif menu_choice == "D":
            display_projects()
        elif menu_choice == "F":
            filter_projects()
        elif menu_choice == "A":
            add_new_project()
        elif menu_choice == "U":
            update_projects()
        else:
            print("Invalid menu choice")
        menu_choice = input(">>> ").upper()


def load_file(filename, projects):
    """Load file and store in a list."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))


def save_project():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_new_project():
    pass


def update_projects():
    pass


main()
