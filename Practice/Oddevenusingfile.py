import random

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()


data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")
l=data.read().split(",")[:-1]

for i in l:
    
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

    if int(i)%2!=0:
        for j in range(3,int(int(i)/2)+1,2):
                if int(i)%j==0:
                  break
        else:
            prime.write(i+",") 
               
            
even.close()
odd.close()
data.close()
prime.close()


data=open("data.txt","r")
print("data is : ")
print(data.read())
data.close()
print("*************************************")

even=open("even.txt","r")
print("even is : ")
print(even.read())
even.close()
print("*************************************")

odd=open("odd.txt","r")
print("odd is : ")
print(odd.read())
odd.close()
print("*************************************")



prime=open("prime.txt","r")
print("prime is : ")
print(prime.read())
prime.close()
print("*************************************")
