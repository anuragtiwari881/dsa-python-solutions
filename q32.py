def first_unique_char(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1

s = "leetcode"
print(first_unique_char(s))