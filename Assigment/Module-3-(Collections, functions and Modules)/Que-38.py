#Write a Python program to check multiple keys exists in a dictionary



dictionary = {"a": 1,"b": 2, "c": 3, "d": 4, "e": 5}
sub_dic=["a","b"]
for key in sub_dic:
    if key not in dictionary:
        print("not multiple key")
        break
else:
    print("multiple key")

