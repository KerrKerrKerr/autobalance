#from dfg import main
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list2 = [0,"H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl",'Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe']  
def second_check(x):
    d={}
    while len(x)!=0:
        a=x[0]
        print(a)
        if a in list2:
            try:
                d[a]=d[a]+1
            except:
                d[a]=1
        else:
            a=a+' '
            a=list(a)
            if a[1]not in n:
                a[0]=a[0]+a[1]
            if (a[1] in n) and (a[2] not in n):
                try:
                    d[a[0]]=d[a[0]]+int(a[1])
                except:
                    d[a[0]]=int(a[1])
            elif a[1] in n and a[2] in n:
                try:
                    d[a[0]]=d[a[0]]+int(a[1]+a[2])
                except:
                    d[a[0]]=int(a[1]+a[2])
            elif (a[2] in n) and (a[3] not in n):
                try:
                    d[a[0]]=d[a[0]]+int(a[2])
                except:
                    d[a[0]]=int(a[2])
            elif a[2] in n and a[3] in n:
                try:
                    d[a[0]]=d[a[0]]+int(a[2]+a[3])
                except:
                    d[a[0]]=int(a[2]+a[3])
        x.pop(0)
    return d

def main(input):
    input = input.split('=>')
    i1, i2 = input[0], input[1]
    i1, i2 = i1.split('+'), i2.split('+')
    i1_2=i1.copy()
    def k_delete(y):
        l1 = []
        while len(y) > 0:
            a = y[0]
            while len(a) > 0:
                if a[0] in n:
                    a = a.replace(a[0], '', 1)
                else:
                    l1.append(a)
                    break
            y.pop(0)
        return l1
    def k_extract(kex):
        e1= []
        u=kex
        while len(u) > 0:
            e2=''
            a = u[0]
            while len(a) >= 1:
                if a[0] in n:
                    e2=e2+str(a[0])
                    a = a.replace(a[0], '', 1)
                else:
                    if len(e2)==0:
                        e2=1
                    e2=int(e2)
                    break
            u.pop(0)
            e1.append(e2)
        print(e1)
        return e1

    print(i1)
    def assemble(l1,l2):
        st=''
        while len(l1)>0 and len(l2)>0:
            st=st+str(l1[0])+str(l2[0])
            if len(l1)>=2:
                st=st+'+'
            l1.pop(0),l2.pop(0)
        return st
    print(assemble(k_extract(i1),k_delete(i1_2)))
    print(i1_2)
main(str(input()))
