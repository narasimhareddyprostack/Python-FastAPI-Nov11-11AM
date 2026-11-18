def login(name,status):
    if status == True:
        print(name, "-:Login Success")
    else:
        print("Login Failed")

login(name="Rahul",status=True)
login(status=True,name="Rahul")