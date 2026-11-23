employees=[
    {"eid":101,"ename":"RG","gender":"Male"},
    {"eid":102,"ename":"Aarav","gender":"Male"},
    {"eid":103,"ename":"Diya","gender":"Female"},
    {"eid":104,"ename":"Kabir","gender":"Male"},
    {"eid":105,"ename":"Ananya","gender":"Female"},
    {"eid":106,"ename":"Vihaan","gender":"Male"},
    {"eid":107,"ename":"Ishita","gender":"Female"},
    {"eid":108,"ename":"Arjun","gender":"Male"},
    {"eid":109,"ename":"Meera","gender":"Female"},
    {"eid":110,"ename":"Rohan","gender":"Male"},
    {"eid":111,"ename":"Saanvi","gender":"Female"},
    {"eid":112,"ename":"Aditya","gender":"Male"},
    {"eid":113,"ename":"Kavya","gender":"Female"},
    {"eid":114,"ename":"Yash","gender":"Male"},
    {"eid":115,"ename":"Nisha","gender":"Female"},
    {"eid":116,"ename":"Rahul","gender":"Male"},
    {"eid":117,"ename":"Pooja","gender":"Female"},
    {"eid":118,"ename":"Amit","gender":"Male"},
    {"eid":119,"ename":"Neha","gender":"Female"},
    {"eid":120,"ename":"Karan","gender":"Male"},
    {"eid":121,"ename":"Sneha","gender":"Female"},
]
#create new employee with new propety loc=Banaglore
new_employees=[]

i=0
while i<=len(employees)-1:
    employees[i]['loc']="Bangalore"
    new_employees.append(employees[i])
    i=i+1

print(new_employees)