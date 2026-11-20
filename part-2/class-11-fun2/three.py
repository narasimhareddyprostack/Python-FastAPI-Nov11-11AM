prices=[98,198,298,398,498]

def plusone(price):
    return price+1

map_obj=map(plusone,prices)

new_prices=list(map_obj)

print(prices)
print(new_prices)