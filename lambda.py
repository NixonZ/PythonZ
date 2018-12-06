def func(n):
    return lambda a : a**n
x=int(input("Enter the power:"))
pow=func(x)
y=int(input("Enter the base:"))
print(pow(y))
z=input()
