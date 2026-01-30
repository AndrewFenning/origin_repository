def making_dictionary_of_strings(list_of_strings):
    dictionary_of_strings = {}
    for string_in_list in list_of_strings:
        length_of_string_i = len(string_in_list)
        dictionary_of_strings[string_in_list] = {"length": length_of_string_i}
        if length_of_string_i % 2 == 0:
            dictionary_of_strings[string_in_list]["parity"] = "even"
        else:
            dictionary_of_strings[string_in_list]["parity"] = "odd"
        #looking at example to confirm what the output should do ("data": {"length": 4, "parity": "even"})

    return dictionary_of_strings

print(making_dictionary_of_strings(["hello", "hi"]))