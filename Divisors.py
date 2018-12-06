x=int(input("Enter a number:"))
list=[]
for y in range(2,x+1):
    if not(x%y):
        list.append(y)
    else:
        continue
print(list)
y=input()
