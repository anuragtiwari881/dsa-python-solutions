def move_hash_front(s):
    count = s.count('#')
    new_string = s.replace('#','')

    return '#' * count + new_string


s = "Move#Hash#to#Front"

print(move_hash_front(s))