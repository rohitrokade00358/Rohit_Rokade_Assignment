a = int(input("Enter a number: "))

if a <= 0:
    print("Please enter a number greater than 0.")
else:
    number = 1
    count = 0

    while count < a:
        print(number, end=", " if count < a - 1 else "")
        number = number + 2
        count = count + 1
