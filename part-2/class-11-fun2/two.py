prices=[98,198,298,398,498]
#create new list of product prices by adding +1 for every price

new_prices=[]

i=0  #initilization 
while i<=len(prices)-1:
    new_prices.append(prices[i]+1)
    i=i+1


print(prices)
print(new_prices)
