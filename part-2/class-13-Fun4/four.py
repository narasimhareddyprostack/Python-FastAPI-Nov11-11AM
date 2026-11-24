a=10        #global scope

def add():
    global b
    b=20     
    print(a+b) 

add()

def multi():
    print(a*b)    #NameError

multi()
#how to convert local variable to global? using global keyword