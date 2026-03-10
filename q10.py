n = int(input("Enter number of elements: "))
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key in sorted(freq):
    print(key, "occurs", freq[key], "times")