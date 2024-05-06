rno=int(input("enter your number"))
name=input("enter your name")
s1=int(input("enter your marks 1"))
s2=int(input("enter your marks 2"))
s3=int(input("enter your marks 3"))

total=s1+s2+s3
per=total/3

print("roll no",rno)
print("student name ",name)
print("total is",total)
print("percantage",per)

if per>=70:
    print("Distincation")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
else:
    print("fail")
