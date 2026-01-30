def x_to_the_power_of_y(list_of_x_and_y):
    result = []
    for each_pair in list_of_x_and_y:
        result.append(each_pair[0]**each_pair[1])
    return result

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
print(x_to_the_power_of_y(pairs))