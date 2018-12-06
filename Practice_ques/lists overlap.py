A=[1,3]
B=[2,4,3,5]
C=[]
'''if len(A)>len(B):
    for x in A:
        for y in B:
            if x==y:
                C.append(x)
                break
else:
    for x in B:
        for y in A:
            if x==y:
                C.append(x)
                break'''
C=[x for x in A if x in B]
print(C)
