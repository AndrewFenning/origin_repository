from random import random

values = [random() for i in range(20)]
x = random()
values.sort()

def finding_the_index_of_the_first_random_number_greater_than_x(list_of_random_numbers, random_number_x):
    for index_of_random_number in range(0,len(list_of_random_numbers)):
        if list_of_random_numbers[index_of_random_number] >= random_number_x:
            return index_of_random_number
    return "none in list greater than x"


print(values)
print(x)
print(finding_the_index_of_the_first_random_number_greater_than_x(values,x))
