from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        else:
            print("Invalid option.")
        print(f"Bill to date ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost ${total_bill:.2f}")
    display(taxis)


def drive_taxi(current_taxi, total_bill):
    """Drive taxi and bill user based on distance."""
    if current_taxi:
        current_taxi.start_fare()
        distance_choice = float(input("Drive how far? "))
        current_taxi.drive(distance_choice)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


def choose_taxi(taxis):
    """Get taxi choice with exception handling."""
    print("Taxis available:")
    display(taxis)
    taxi_choice = int(input("Choose taxi: "))

    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
        return None
    # print(current_taxi)


def display(taxis):
    """Display a list of taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
