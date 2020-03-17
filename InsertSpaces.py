def insert_spaces(s, width):
    if len(s) >= width:
        return s

    space_count = s.strip().count(" ")
    space_arr = [1] * space_count
    num_of_spaces_to_add = width - len(s)

    i = 0
    while True:
        space_arr[i] += 1
        num_of_spaces_to_add -= 1
        if num_of_spaces_to_add == 0:
            break
        if i == len(space_arr) - 1:
            i = 0
        else:
            i += 1

    split_arr = s.split()
    output = ""
    for i in range(len(split_arr)):
        if i == len(split_arr) - 1:
            output += split_arr[i]
        else:
            output += split_arr[i] + " " * space_arr[i]
    return output.strip()


print(insert_spaces("the quick brown fox", 23))
