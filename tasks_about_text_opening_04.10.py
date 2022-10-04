# Exercise
# read text from  sherlock_holmes_adventures.txt
# import pathlib
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len("sherlock_holmes_adventures.txt") -> 12305

with open("Day12_File_Operations\sherlock_holmes_adventures_1661-0.txt", "r", encoding="utf-8") as fstream:
    count = 0
    for line in fstream:
        count += 1

print("Total amount of lines are:", count)

# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

with open("Day12_File_Operations\sherlock_holmes_adventures_1661-0.txt", "r", encoding="utf-8") as fstream:
    count = 0
    for line in fstream:
        if line != "\n":
            count += 1  # did not need the count, just wanted to check
            print(line)
    print(count)


# 1c -> write the function save_lines(destpath, lines)


# with open("Day12_File_Operations\sherlock_holmes_adventures_1661-0.txt", "r", encoding="utf-8") as fstream:

# This function will store all lines into destpath file

# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")

# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary
