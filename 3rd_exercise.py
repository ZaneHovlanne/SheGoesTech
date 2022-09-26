def clean_dict_value(d, bad_val):
    cleaned_dictionary = {}
    for i in list(d):
        if d[i] == bad_val:
            del d[i]
        else:
            cleaned_dictionary[i] = d[i]
    print(cleaned_dictionary)


clean_dict_value({'a': 7, 'b': 6, 'c': 9}, 7)
