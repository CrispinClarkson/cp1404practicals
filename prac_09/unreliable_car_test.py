from prac_09.unreliable_car import UnreliableCar


def main():
    great_car = UnreliableCar("Toyota Corolla", 100, 90)
    bad_car = UnreliableCar("LandCruiser FJ45", 100, 10)

    for i in range(1, 15):
        print(f"Driving {i}km")
        print(f"{great_car.name:15} drove {great_car.drive(i):3}km")
        print(f"{bad_car.name:15} drove {bad_car.drive(i):3}km")

    print(great_car)
    print(bad_car)


if __name__ == '__main__':
    main()
