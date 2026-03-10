month = int(input("Enter month: "))

if month < 1 or month > 12:
    print("Invalid Month Entered")

elif month in [3,4,5]:
    print("Season: Spring")

elif month in [6,7,8]:
    print("Season: Summer")

elif month in [9,10,11]:
    print("Season: Autumn")

else:
    print("Season: Winter")