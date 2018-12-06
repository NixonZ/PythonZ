#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
x=int(input("Enter a number:"))
if x%2:
    print("Odd")
elif not(x%4):
    print("Multiple of 4")
else :
    print("Even")
num=int(input("Enter num:"))
check=int(input("Enter check:"))
if not(num%check):
    print(str(check)+" divides "+str(num))
else:
    print(str(check)+" does not divide "+str(num))
z=input()
