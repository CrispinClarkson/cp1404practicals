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
            if current_taxi:
                current_taxi.start_fare()
                distance_choice = float(input("Drive how far? "))
                current_taxi.drive(distance_choice)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")

        elif choice == "c":
            print("Taxis available:")
            display(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
            # print(current_taxi)
        else:
            print("Invalid option.")
        print(f"Bill to date ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost ${total_bill:.2f}")
    display(taxis)


def display(taxis):
    """Display a list of taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
