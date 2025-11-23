from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Silver service taxi test program."""
    my_silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi)
    print(my_silver_service_taxi.get_fare())


if __name__ == '__main__':
    main()
