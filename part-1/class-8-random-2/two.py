def calc(a,b,op):

    if op=="sum":
        return a+b 
    if op=="sub":
        return a-b 
    else:
        return 0


result=calc(10,20,"div")
print(result)