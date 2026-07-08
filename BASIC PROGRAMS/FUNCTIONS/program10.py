def parva(func):
    def inner(x):
        return func(x).upper()
    return inner

@parva
def priyanshu(name):
    return "HI! MY NAME IS " + name

print(priyanshu("PARVA SHARMA"))