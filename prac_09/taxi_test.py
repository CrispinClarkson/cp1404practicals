from prac_09.taxi import Taxi


def main():
    """Taxi test program."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}, ${my_taxi.get_fare()}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, ${my_taxi.get_fare()}")


if __name__ == '__main__':
    main()
