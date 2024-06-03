#Write python program that user to enter only odd numbers, else will raise an exception
while True:
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("Please enter an odd number.")
        else:
            print("You entered:", num)
            break
    except ValueError as e:
        print(e)
