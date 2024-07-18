#Write a Python program to count the occurrences of each word in a given sentence
def word_count(a):
    counts = {}
    words = a.split()
    for word in words:
        word = word.lower() 
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
a = "hello how are you.what Are you doing"
word_frequencies = word_count(a)
for word, count in word_frequencies.items():
    print(f"{word}: {count}"
