first = input("Please enter your first name: ")
second = input("Please enter your second name: ")
second = str(second) + "!"
max_star = max (len(first),len(second),len("Hello,"))

print("*" * 3 + "*" * max_star + "*" * 3)
print("*" * 2 + " " + "Hello," + " " * (max_star - len("Hello,")) + " " + "*" *2)
print("*" * 2 + " " + first + " " * (max_star - len(first)) + " " + "*" *2)
print("*" * 2 + " " + second + " " * (max_star - len(second)) + " " + "*" *2)
print("*" * 3 + "*" * max_star + "*" * 3)