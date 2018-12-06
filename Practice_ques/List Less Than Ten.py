
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

i=int(input("Enter a number:"))
newlist=[]
for x in a:
    if x<i:
        newlist.append(x)
print(newlist)        
z=input()
