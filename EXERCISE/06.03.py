x=input("Enter the first number: ")
print(x)
x=float(x)
y=input("Enter the second number: ")
print(y)
y=float(y)
if x>10 and y>10:
    print("Both are above 10.")
elif x<=10 and y<=10:
    print("Both are below 10.")
z=(x+y)/2
print("Average is",round(z,2))

    