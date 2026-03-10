def count_pairs(arr, target):
    count = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1

    return count


arr = [1,5,7,-1,5]
target = 6

print(count_pairs(arr, target))