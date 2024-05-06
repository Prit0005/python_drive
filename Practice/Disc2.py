d={1:"jigar",2:"ajay",3:"kamal",4:"ketan",5:"sunil"}

value=input("enter values to search from disctonary :")

flag=False
for i in d:
    if d[i]==value:
        flag=True
        break
if flag==True:
    print(value,"present in disctonary")
else:
    print(value,"not present in disctonary")
    
