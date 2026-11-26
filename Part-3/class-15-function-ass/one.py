a=10
def outer():
    counter=5      #Local variable

    def inner():
        nonlocal counter
        counter=counter+1
        return counter

    return inner()

print(outer())