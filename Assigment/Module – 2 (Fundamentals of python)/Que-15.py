#  Write a Python program to count occurrences of a substring in a string.
# 1.You can use the built-in count() method on a string to find the number of non-overlapping occurrences of a substring.
my_string = "hello how are you"
substring = "o"
count = my_string.count(substring)
print(f"Number of occurrences of '{substring}': {count}")
# 2.For overlapping occurrences: If you need to count overlapping occurrences, you can use a custom function

def find(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

my_string = "madam,mam"
substring = "ma"
overlapping_count = find(my_string, substring)
print(f"Number of overlapping occurrences of '{substring}': {overlapping_count}")

#3. Using regular expressions (with overlapping): You can also use re.findall() to find overlapping occurrences of a substring:

import re
my_string = "hello"
substring = "ll"
overlapping_count = len(re.findall(f'(?=({substring}))', my_string))
print(f"Number of overlapping occurrences of '{substring}': {overlapping_count}")
