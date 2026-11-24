a=10        #global scope

def add():
    b=20     #local scope/variable
    print(a+b) 

add()

def multi():
    print(a*b)    #NameError

multi()
#how to convert local variable to global? using global keyword