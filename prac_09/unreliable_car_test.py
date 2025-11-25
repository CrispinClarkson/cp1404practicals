from prac_09.unreliable_car import UnreliableCar


def main():
    """Unreliable car test program."""
    great_car = UnreliableCar("Toyota Corolla", 100, 90)
    bad_car = UnreliableCar("LandCruiser FJ45", 100, 10)

    for i in range(1, 15):
        print(f"Driving {i}km")
        print(f"{great_car.name:15} drove {great_car.drive(i):3}km")
        print(f"{bad_car.name:15} drove {bad_car.drive(i):3}km")

    print("Testing 30% reliability:")
    bad_car_worst = UnreliableCar("Vroom Vroom", 100, 30)
    for i in range(1, 15):
        bad_car_worst.drive(5)
        print(f"{bad_car_worst.name} drove {bad_car_worst.drive(i):3}km")

    print()

    print("Testing 60% reliability:")
    bad_car_better = UnreliableCar("Car", 100, 60)
    for i in range(1, 15):
        bad_car_better.drive(5)
        print(f"{bad_car_better.name} drove {bad_car_better.drive(i):3}km")

    print(great_car)
    print(bad_car)


if __name__ == '__main__':
    main()
