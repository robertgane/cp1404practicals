"""
CP1404/CP5632 Practical - Project Management Program.
"""
from prac_07.project import Project
import datetime

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
            filter_projects(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_projects(projects)
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


def filter_projects(projects):
    """Filter projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        projects = sorted(projects, key=lambda x: datetime.datetime.strptime(f"{project.start_date}", "%d/%m/%Y"),
                          reverse=False)
        if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date:
            print(project)


def add_new_project(projects):
    """Add new project to projects"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input(int("Cost estimate:"))
    percent_completed = input(int("Percent complete: ", 100))
    new_project = Project(name, start_date, int(priority), float(cost_estimate), int(percent_completed))
    projects.append(new_project)
    print(f"{name} project added.")


def update_projects(projects):
    """Update project by user choice."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    index = get_valid_number("Project choice: ", len(projects) - 1)
    print(projects[index])
    new_percentage = get_valid_number("New Percentage (0-100): ", 100)
    new_priority = get_valid_number("New Priority(0-9): ", 9)
    projects[index].priority = new_priority
    projects[index].percentage_completed = new_percentage
    print(f"project {index} updated.")


def get_valid_number(prompt, maximum_value):
    """Get valid number from user."""
    is_finished = False
    number = 0
    while not is_finished:
        try:
            number = int(input(prompt))
            while number < 0 or number > maximum_value:
                if number < 0:
                    print("Number must be >= 0")
                elif number >= maximum_value:
                    print("Number out of range")
                number = int(input(prompt))
            is_finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


main()
