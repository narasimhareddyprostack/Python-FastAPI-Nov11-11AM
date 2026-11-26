eids={101,102,103,104}

#set.remove() vs set.discard()
#eids.remove(104)
#eids.discard(104)

#eids.remove(109) # if element not present - KeyError  
eids.discard(109) #if element not present - no error
print(eids)