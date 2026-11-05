b=bytes([10,20,30,40,255,10,20,30,40,255])
print(b)  #b'\n\x14\x1e(\xff'
print(list(b))
print(set(b))