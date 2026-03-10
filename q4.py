def solve_equation(a, b):
    result = a**3 + a**2*b + 2*a**2*b + 2*a*b**2 + a*b**2 + b**3
    return result


# Input
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))   # accepted as per question

# Function call
ans = solve_equation(a, b)

print("Result:", ans)