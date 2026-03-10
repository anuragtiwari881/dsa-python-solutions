rows, cols = map(int, input("Enter rows and columns: ").split())

matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = rows - 1
left = 0
right = cols - 1

result = []

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)