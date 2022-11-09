"""
CP1404/CP5632 Practical - Project Management Program.
"""
from prac_07.project import Project

FILENAME = "../prac_07/projects.txt"
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- " \
       "(A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Displays project_management program."""
    projects = []
    load_file(FILENAME, projects)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Enter filename to load projects from: ")
            load_file(filename, projects)
        elif menu_choice == "S":
            save_project(FILENAME, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects()
        elif menu_choice == "A":
            add_new_project()
        elif menu_choice == "U":
            update_projects()
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_file(filename, projects):
    """Load file and store in a list."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))


def save_project(filename, projects):
    """Save projects into file"""
    with open(filename, 'w') as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.estimate}\t{project.completion}",
                  file=out_file)


def display_projects(projects):
    """Display projects sorted by priority."""
    projects.sort()
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def filter_projects():
    pass


def add_new_project():
    pass


def update_projects():
    pass


main()
