def rotate_check(s, goal):
    if len(s) != len(goal):
        return False

    return goal in (s + s)


s = "abcde"
goal = "cdeab"

print(rotate_check(s, goal))