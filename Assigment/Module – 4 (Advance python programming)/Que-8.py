#Write a python program to find the longest words.

name="i am pritesh senjaliya"
divide=name.split()
longword=""
for word in divide:
    if len(word)>len(longword):
        longword=word

print(longword)
