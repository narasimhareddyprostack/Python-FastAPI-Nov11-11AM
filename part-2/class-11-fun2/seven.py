numbers=[1,2,3,4]
new_numbers=[]

i=0
while i<=len(numbers)-1:
    new_numbers.append(numbers[i]*numbers[i])
    i=i+1

print(numbers)
print(new_numbers)