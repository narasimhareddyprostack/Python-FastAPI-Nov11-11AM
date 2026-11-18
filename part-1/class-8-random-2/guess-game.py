import random

comp_num=random.randint(1,50)
#print("Computer Number:", comp_num)

while True:

    guessing_num=int(input("Enter Number:"))

    if comp_num>guessing_num:
        print("To LOW... Please Try")
    elif comp_num < guessing_num:
        print("To HIGH ... Please Try")
    else:
        print("Success")
        break
