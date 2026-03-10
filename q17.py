def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)


nums = [3,0,1]

print(missing_number(nums))