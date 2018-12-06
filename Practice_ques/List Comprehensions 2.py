import random
A=random.sample(range(100),random.randint(1,9)) #creates a list
B=random.sample(range(100),random.randint(1,9))
C=[x for x in A if x in B]
print(A)
print(B)
print(C)
