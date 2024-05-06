t=(1,2,1.1,2.2,"tops",[100,200,300],True,0,20,1,2)

print(t)
print(t.count(2))
print(t.index(2))

for i in t:
    print(i)

print(10 in t)

print(t[5])
t[5].append(500)
print(t)
print(t[5][0])
