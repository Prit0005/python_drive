#Write a Python program to count the frequency of words in a file.

file=open("Q-4.txt","r")
read=file.read()
devide=read.split()
word_frequency={}

for word in devide:
    word=word.strip().lower()
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word]=1

for word,frequency in word_frequency.items():
    print(word,":",frequency)
file.close()
