x=input("Enter choice for player 1:")
y=input("Enter choice for player 2:")
z=0
if x==y:
    print("tie")
    exit(1)
    z=input()
if x=='rock':
    if y=='paper':
        z=1
    else:
        z=0
if x=='paper':
    if y=='scissor':
        z=1
    else:
        z=0
if x=='scissor':
    if y=='rock':
        z=1
    else:
        z=0
if z==1:
    print('player2 wins')
else:
    print('player1 wins')
z=input()
