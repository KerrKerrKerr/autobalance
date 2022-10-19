list2 = [0,"H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl",'Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe']      
list3 = [0,1,4,7,9,11,12,14,16,19,20,23,24,27,28,31,32,35.5,40,39,40,45,48,51,52,55,56,59,59,63.5,65]
n=['0','1','2','3','4','5','6','7','8','9']
def main(x):
    def el(y):     #ищeм количество элементов
        print(y)
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
                            if x[1].isupper() or x[1]=='/' and not x[1]in n:    #C
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
            y.remove(y[0])    
        return moles
    halfes=x.split('=>')
    fst,scnd=halfes[0],halfes[1]
    fst=fst.replace(" ", "")
    scnd=scnd.replace(' ','')
    fst=fst.split('+')
    scnd=scnd.split('+')
    def second_check(x):
        n=['0','1','2','3','4','5','6','7','8','9']
        d={}
        x=el(x)
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
    f1=second_check(fst)
    s1=second_check(scnd)
    print(f1,s1)
    if (s1==f1):
        print('success')
        return 1
    else:
        return 0
