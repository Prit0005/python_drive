#Write a Python program to calculate surface volume and area of a cylinder

radius = int(input("enter the radius of the base of the cylinder: "))
height = int(input("enter the height of the cylinder: "))

area=2 * 3.14 * radius * (radius + height)
print("area : ",area)
surface_volume=3.14 * radius ** 2 * height
print("surface volume : ",surface_volume)
