arr = list(map(int, input("Enter array elements: ").split()))

unique = sorted(set(arr))

if len(unique) < 2:
    print("Second Smallest :", -1)
    print("Second Largest :", -1)
else:
    print("Second Smallest :", unique[1])
    print("Second Largest :", unique[-2])