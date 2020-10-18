def drive(car_name, distance, fuel_quantity):
    if fuel_quantity > cars[car_name][1]:
        result = -1
    else:
        cars[car_name][0] += distance
        cars[car_name][1] -= fuel_quantity
        result = 1
        if cars[car_name][0] >= 100000:
            cars.pop(car_name)
            result = -10
    return result


def refuel(car_name, fuel_quantity):
    if cars[car_name][1] + fuel_quantity > 75:
        temp = 75 - cars[car_name][1]
    else:
        temp = fuel_quantity
    cars[car_name][1] += temp
    return temp


def revert(car_name, kilometers):
    cars[car_name][0] -= kilometers
    if cars[car_name][0] < 10000:
        cars[car_name][0] = 10000


n = int(input())

cars = {}

for _ in range(n):
    data = input()
    split_data = data.split("|")
    car = split_data[0]
    mileage = int(split_data[1])
    fuel = int(split_data[2])

    cars[car] = [mileage, fuel]

while True:
    data = input()
    if data == "Stop":
        break
    split_data = data.split(" : ")
    command = split_data[0]
    if command == "Drive":
        car = split_data[1]
        distance = int(split_data[2])
        fuel = int(split_data[3])
        drive_res = drive(car, distance, fuel)
        if drive_res == -1:
            print("Not enough fuel to make that ride")
        elif drive_res == -10:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            print(f"Time to sell the {car}!")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    elif command == "Refuel":
        car = split_data[1]
        fuel = int(split_data[2])
        res_refuel = refuel(car, fuel)
        print(f"{car} refueled with {res_refuel} liters")

    elif command == "Revert":
        car = split_data[1]
        kilometers = int(split_data[2])
        revert(car, kilometers)
        if cars[car][0] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")

sorted_cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))

for car, info in sorted_cars.items():
    print(f"{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.")
    