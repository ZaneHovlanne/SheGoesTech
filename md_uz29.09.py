# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af"
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊


def lexigraphically_ordered_string(good_string1, good_string2, bad_string):
    good_string1_set = set(good_string1)
    good_string2_set = set(good_string2)
    bad_string_set = set(bad_string)
    result = ((good_string1_set & good_string2_set) - bad_string_set)
    return result


print(lexigraphically_ordered_string("fab", "abcdf", "boo"))
