def ispall(string):
    test=1
    length=len(string)
    for x in range(length//2):
        if string[x]!=string[length-x-1]:
            test=0
            break
        else:
            continue
    return test
x=input("Enter a string:")
if ispall(x):
    print("Pallindrome")
else:
    print("Not Pallindrome")
y=input()
