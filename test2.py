from fun import *
from itertools import combinations_with_replacement

def p_(lst):
    def p(o):
        return sum(o)
    r_list=[[1]*len(lst[0])]
    for i in range(len(lst)):
        if (lst[0]).count((lst[0])[0])!=len(lst[0]):
                lst[0]=list(lst[0])
                for l in range(len(lst[0])):
                    state = False
                    lst[0].append((lst[0])[0])
                    lst[0].pop(0)
                    r_list.append(lst[0].copy())
                    if len(lst[0])>=3 and state==False and (lst[0]).count((lst[0])[0])!=len(lst[0])-1 :
                        #print((lst[0]).count((lst[0])[0])!=len(lst[0]),lst[0],len(lst[0]))
                        for t in range(len(lst[0])):
                            lst[0].append((lst[0])[0+t-1])
                            lst[0].pop(0+t-1)
                            r_list.append(lst[0].copy())   
                            if t == (len(lst[0])-1):
                                state=True     
                                break              
        
        lst.pop(0)
    r_list.sort(key=p)
    return r_list
print(p_(list(combinations_with_replacement(nn,3))))
