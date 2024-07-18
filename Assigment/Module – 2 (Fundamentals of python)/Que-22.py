# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, returninstead of the empty string.

def get_modified_string(input_string):
    if len(input_string) < 2:
        return ""
    else:
        return input_string[:2] + input_string[-2:]

# Example usage:
user_input = input("Enter a string: ")
result = get_modified_string(user_input)
print("Modified string:", result)
