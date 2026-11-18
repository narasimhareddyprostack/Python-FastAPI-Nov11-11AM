#Select lucky dip member from below names

import random

enames=["Arunima","Sonal","Purna","Pavan","Ravi","Vaishnavi","Rahul","Sonia","Priyanka","Modi"]

first_3_names=random.choices(enames,k=3)

print("Lucky Member's Today is:", first_3_names)
