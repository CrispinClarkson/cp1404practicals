"""
Estimated Time: 2:30 hours
Actual Time: 5 hours
"""
from datetime import datetime
from operator import attrgetter
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
            start_date = datetime.strptime(start_date, "%d/%m/%Y")

            projects.append(Project(name, start_date, priority, cost_estimation, completion_percentage))
    return projects


def save_projects(projects):
    """Save current projects to file."""
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
    """Filter projects by date and display projects after date."""
    filter_date = input("Show projects that start after date (dd/mm/yyyy): ")

    if filter_date == "":
        print("No dates entered")
        return

    try:
        filter_converted = datetime.strptime(filter_date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date")
        return

    for project in sorted(projects, key=attrgetter("start_date")):
        if project.start_date >= filter_converted:
            print(project)


def add_projects(projects):
    """Add new projects into list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    start_date_converted = datetime.strptime(start_date, "%d/%m/%Y")
    priority = get_valid_number("Priority: ", 0, 10)
    cost_estimation = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Percent Complete: "))
    projects.append(Project(name, start_date_converted, priority, cost_estimation, completion_percentage))


def update_projects(projects):
    """Update projects and change percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = get_valid_number("Project choice: ", 0, len(projects) - 1)
    selected_project = projects[project_choice]
    print(selected_project)

    new_percentage = get_valid_number("New Percentage: ", 0, 100)
    new_priority = input("New Priority: ")

    if new_percentage != "":
        selected_project.completion_percentage = int(new_percentage)
    if new_priority:
        selected_project.priority = int(new_priority)


def quit_projects(projects):
    """Quit projects and ask user if they want to save to file."""
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").upper()
    if save_choice == "Y":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def get_valid_number(prompt, low, high):
    """Get valid integer between low and high from user."""
    number = low
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number < low:
                print(f"Number must be > {low - 1}")
            elif number > high:
                print("Invalid number")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number


main()
