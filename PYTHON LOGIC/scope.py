def fname():
    x="parva"
    def lname():
        nonlocal x
        x="sharma"
    lname()
    return x


print(fname())
