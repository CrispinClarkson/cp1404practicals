"""
Estimated Time: 2:30 hours
Actual Time:
"""

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
            save_projects()
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_projects(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    quit_projects()


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
            projects.append(Project(name, start_date, priority, cost_estimation, completion_percentage))
    return projects


def save_projects():
    pass


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


def filter_projects():
    """Filter projects by date."""
    pass


def add_projects(projects):
    """Add new projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
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


def quit_projects():
    """Quit projects."""
    pass


main()
