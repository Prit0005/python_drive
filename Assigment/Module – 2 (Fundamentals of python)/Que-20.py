# Write a Python function that takes a list of words and returns the length of the longest one.

def check(words):
    if not words:
        return 0
    longest_length = max(len(word) for word in words)
    return longest_length

word_list = ["ankit", "bhavin", "kishanbhai", "pritesh"]
print(check(word_list))
