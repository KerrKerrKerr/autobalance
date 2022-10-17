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


x=str(input())
x=x.split('=>')
x1,x2=x[0],x[1]
x1,x2=x1.split('+'),x2.split('+')
def smt(x):
    d=[]
    p1=[]
    while len(x)!=0:
        x0=x[0]
        if x0[0] not in n:
            p=[1]
        else:
            p=[]
            while len(x0)!=0:
                if x0[0]in n:
                    p.append(str(x0[0]))
                    x0=x0[1:len(x0)]
                else:
                    p1.append(p[0:len(p)])
                    break
        d.append(x0)
        x.pop(0)

def main(input):
    input = input.split('=>')
    i1, i2 = input[0], input[1]
    i1, i2 = i1.split('+'), i2.split('+')
    i1_2=i1
    def k_delete(kdl):
        l1 = []
        while len(kdl) > 0:
            a = kdl[0]
            while len(a) > 0:
                if a[0] in n:
                    a = a.replace(a[0], '', 1)
                else:
                    l1.append(a)
                    break
            kdl.pop(0)
        return l1
    def k_extract(kex):
        e1= []
        while len(kex) > 0:
            e2=''
            a = kex[0]
            while len(a) >= 1:
                if a[0] in n:
                    e2=e2+str(a[0])
                    a = a.replace(a[0], '', 1)
                else:
                    if len(e2)==0:
                        e2=1
                    e2=int(e2)
                    break
            kex.pop(0)
            e1.append(e2)
        return e1

    koefs=k_extract(i1)
    for t in koefs:
        for t in range(10):
            print('aaaa',t)

main(input(str()))
