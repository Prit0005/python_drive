s=input("enter your string :")


al=0
up=0
low=0
for i in s:
    if i.isalpha():
        al=al+1
    if i.isupper():
       up=up+1
    if i.islower():
        low=low+1
        
print("character :",al)
print("space",s.count(" "))
print("uppercase :",up)
print("lowercase :",low)

    


