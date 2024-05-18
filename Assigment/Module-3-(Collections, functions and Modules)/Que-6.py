'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.'''

string_list=["121","xyx","567","989","bevb"]


def comparision(string_list):
    counter=0
    for string in string_list:
        if len(string)>=2 and string[0]==string[-1]:
            counter+=1
    return counter

result=comparision(string_list)

print("first and last character are same string are : ",result)
