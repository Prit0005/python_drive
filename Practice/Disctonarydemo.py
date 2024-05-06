d={101:"akshy",345:"jeet",909:"Nishant",876:"raj",900:"rahul",567:"pritesh"}

print(d)
print(d[567])
print(d.get(567))
print(d.items())
print(d.keys())
print(d.values())
d.pop(900)
print(d)
d.popitem()
print(d)
d1={900:"rahul",567:"pritesh",432:"nandini",989:"urvi"}
d.update(d1)
print(d)
d[111]="jigar"
print(d)


for i in d:
    print(i," : ",d[i])
