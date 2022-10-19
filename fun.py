n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nn=[1,2,3,4,5,6,7,8,9]
list2 = [0,"H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl",'Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe']  
def assemble(l1,l2): #первый список коэфы. второй вещества после k_delete
    st=''
    while len(l1)>0 and len(l2)>0:
        st=st+str(l1[0])+str(l2[0])
        if len(l1)>=2:
            st=st+'+'
        l1.pop(0),l2.pop(0)
    return st

def k_extract(kex): #зачем-то парился над функцией чтобы ни разу не вызвать... по аналогии k_delete только в выходе одни коэфы
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

def k_delete(y): #на ввод список ОБЩИЙ без лишнего, на выходе список без коэфициентов
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

def second_check(x): #на ввод список с одной из сторон уравнения, на вывод словарь с учетом уоэфициентов
    n=['0','1','2','3','4','5','6','7','8','9']
    d={}
    x=el(x)
    while len(x)!=0:
        a=x[0]
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
    print(d)
    return d

def smt(x): #не знаю что это но это было в файле и нигде не вызывалось
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

    return p1

def new(inp): #я не знаю что это
    inp.split('=>')
    i1, i2 = inp[0], inp[1]
    i1, i2 = i1.split('+'), i2.split('+')

def el(y):     #ищeм количество элементов, нужна чтобы second_check работал
    moles=[]
    while len(y)>0:
        x=y[0]
        n=['0','1','2','3','4','5','6','7','8','9']
        if len(x)==0 :
            print('you haven`t print anything or done something wrong')
            return 0
        koef=int(1)
        if x[0] in n and x[1] in n:
            x="".join(x)
            koef=x[0:2]
            x=x.replace(koef,'',1)
            koef=int(koef)
        if x[0] in n and x[1] not in n:
            koef=x[0]
            x=x.replace(koef,'',1)
            koef=int(koef)
        if len(x)!=0:
            x="".join(x)
            x=x+'//'
            x=list(x)
            while x[0]!='//' and x[0]!='///' and x[0]!='/' :
                if x[0].islower() or x[0]in n:
                        x.remove(x[0])
                else:
                    if x[0].isupper:
                        if (x[1].isupper()) or x[1]=='/' and not x[1]in n:    #C
                            current=x[0]+str(koef)
                            moles.append(current)
                        elif x[1] in n and x[2] in n:   #C12
                            current=x[0]=str(int(x[1])+int(x[2])*koef)
                            moles.append(current)
                        elif x[1] in n and x[2] not in n :   #C6
                            current=x[0]+str(int(x[1])*koef)
                            moles.append(current)
                        elif x[1].islower() and x[2].isupper() and not x[2] in n:     #CaC
                            current=(x[0]+x[1])+str(koef)
                            moles.append(current)
                        elif x[1].islower() and x[2]in n and not x[3]in n:   #Ca6
                            current=(x[0]+x[1])+str(int(x[2])*koef)
                            moles.append(current)
                        elif x[1].islower() and x[2]in n and x[3]in n:   #Ca12
                            current=(x[0]+x[1])+str(int(int(x[2]+x[3])*koef))
                            moles.append(current)
                        elif x[1].islower() and (x[2]=='/'or x[2].isupper()) :    #Ca
                            current=(x[0]+x[1])+str(koef)
                            moles.append(current)
                        currnet=''
                        x.remove(x[0])
        y.pop(0)   
    return moles