#Write a Python script to sort (ascending and descending) a dictionary by value

input_dict = {'english': 90, 'gujrati': 80, 'hindi': 95, 'maths': 75}

desc = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))

asc = dict(sorted(input_dict.items(), key=lambda item: item[1]))

print("Descending order:", desc)
print("Ascending order:",asc)
