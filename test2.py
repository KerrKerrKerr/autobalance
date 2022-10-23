list = [1,1,1,2,3]
l=[]
for i in range(len(list)):
    list.append(list[0])
    list.pop(0)
    l.append(list.copy())
    print(l)
