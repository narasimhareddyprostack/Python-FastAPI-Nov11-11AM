eids=[101,102,103,104,101,101,104]
#index 0  1    2   3   4   5   6
print(eids.index(104))
print(eids.count(104))
#update
eids.append(105)
print(eids)
eids.insert(1,100)
print(eids)  
eids.extend([106,107,108])
print(eids)
#delete

eids.pop()
print(eids)
eids.remove(104)
print(eids)
del eids 
print(eids)