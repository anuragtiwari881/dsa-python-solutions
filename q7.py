num = int(input("Enter number: "))

if num == 0:
    print("No Factors")
else:
    num = abs(num)
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    print(",".join(map(str, factors)))