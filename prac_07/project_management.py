"""
Estimated Time: 2:30 hours
Actual Time:
"""
import datetime
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = ("- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date"
        "\n- (A)dd new projects \n- (U)pdate project \n- (Q)uit")


def main():
    """Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects loaded from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(filename=DEFAULT_FILENAME)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_projects(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    quit_projects(projects)


def load_projects(filename=DEFAULT_FILENAME):
    """Load projects from file."""
    projects = []
    with open(filename, "r") as input_file:
        input_file.readline()
        for line in input_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = (parts[1])
            priority = int(parts[2])
            cost_estimation = float(parts[3])
            completion_percentage = int(parts[4])
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()

            projects.append(Project(name, start_date, priority, cost_estimation, completion_percentage))
    return projects


def save_projects(projects):
    save_file = input("What file would you like to save to? ")
    with open(save_file, "w") as output_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                  f"\t{project.cost_estimation}\t{project.completion_percentage}", file=output_file)
        print(f"{len(projects)} projects saved to {save_file}")


def display_projects(projects):
    """Display projects and format through complete and incomplete projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete_projects):
        print(f"  {project}")


def filter_projects(projects):
    """Filter projects by date."""


def add_projects(projects):
    """Add new projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    start_date_converted = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimation = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Percent Complete: "))
    projects.append(Project(name, start_date, priority, cost_estimation, completion_percentage))


def update_projects(projects):
    """Update projects."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project Choice: "))
    selected_project = projects[project_choice]
    print(selected_project)

    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))

    if new_percentage != "":
        selected_project.completion_percentage = int(new_percentage)
    if new_priority:
        selected_project.priority = int(new_priority)


def quit_projects(projects):
    """Quit projects."""
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ")
    if save_choice == "Y":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


main()
