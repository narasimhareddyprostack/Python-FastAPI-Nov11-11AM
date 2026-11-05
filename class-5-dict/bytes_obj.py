b=bytes([10,20,30,40,255])
print(b)  #b'\n\x14\x1e(\xff'

#reading bytes object element - using indexing
print(b[4])

#print all bytes object values
for ele in b:
    print(ele)