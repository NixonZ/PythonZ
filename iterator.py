from recursion import factorial
class pattern:
    var=0
    """docstring for pattern."""
    def __init__(this,x):
        this.var=x
    def __iter__(this):
        return this
    def __next__(this):
        if this.var<=5:
            this.var+=1
        else:
            raise StopIteration
        return factorial(this.var)
foo=pattern(0)
iterator=iter(foo)
for x in iterator:
    print(next(iterator))
