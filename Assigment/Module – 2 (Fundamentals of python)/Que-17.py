#  Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

def swap_first_two_chars(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least two characters."
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    combined_string = new_str1 + " " + new_str2
    return combined_string

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = swap_first_two_chars(str1, str2)
print("Resulting string:", result)
