def calculate_tyres():
    n = int(input("Enter number of dealerships: "))

    for i in range(n):
        cars, bikes = map(int, input().split())

        tyres = (cars * 4) + (bikes * 2)

        print(tyres)


# function call
calculate_tyres()