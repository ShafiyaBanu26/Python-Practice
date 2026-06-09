tuple=(1,"green",3,3)
print("first element:",tuple[0])
print("length:",len(tuple))
print("count of repeated elements")
print("count of 3:",tuple.count(3))
print("count of each elements")
for i in tuple:
    count=0
    if i in tuple:
        count=count+1
    else:
        count=1
for i in tuple:
    print(i,count)
    
           


