#learning classes
class complex:
    """Implementing Complex numbers"""
    real=0
    imag=0
    def __init__(this,real=0,imag=0):
        this.real=real
        this.imag=imag
    def __str__(this):
        return (str(this.real)+'+'+str(this.imag)+'i')
    def update(this,x,y):
        this.real=x
        this.imag=y
    def __add__(this,other):
        return complex(this.real+other.real,this.imag+other.imag)
z=complex(2,3)
z.update(5,6)
k=complex(2,3)
print(k+z)
