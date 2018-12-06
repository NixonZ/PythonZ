import random
a=random.randint(1,9)
x=0
count=0
while x!='exit':
    x=input("Enter a number('exit' to exit)")
    count+=1
    if int(x)>a :
        print("Too high")
    elif int(x)<a:
        print("Too low")
    else:
        print("Exactly right")
        print("Guessed in "+str(count)+" tries")
        break
