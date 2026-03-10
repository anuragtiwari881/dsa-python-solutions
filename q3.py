sem = int(input("Enter no of semester: "))

subjects = []
for i in range(sem):
    n = int(input(f"Enter no of subjects in {i+1} semester: "))
    subjects.append(n)

for i in range(sem):
    marks = list(map(int, input(f"Marks obtained in semester {i+1}: ").split()))

    invalid = False
    for m in marks:
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            invalid = True
            break

    if not invalid:
        print(f"Maximum mark in {i+1} semester:", max(marks))