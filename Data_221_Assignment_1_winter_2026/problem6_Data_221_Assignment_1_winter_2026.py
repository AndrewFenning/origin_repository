
def making_dictionary_out_of_list_for_distribution_analysis(list_of_numbers):
    dictionary = {}

    for number_in_list in list_of_numbers:
        counter_of_number_in_list = 0
        for numbers_in_list in list_of_numbers:
            if numbers_in_list <= number_in_list:
                counter_of_number_in_list += 1
        dictionary[number_in_list] = counter_of_number_in_list/len(list_of_numbers) * 100
    return dictionary

numbers = [3, 1, 2, 3, 4, 2]

print(making_dictionary_out_of_list_for_distribution_analysis(numbers))