n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
x='1ll'
a=''
while len(x)>0:
    if x[0] in n:
        a=a+str(x[0])
        x=x.replace(x[0],'',1)
    else :
        break
print(a)
