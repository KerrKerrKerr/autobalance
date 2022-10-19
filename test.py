""" from itertools import combinations
x=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
y=['first','second','third']
s=0
def assemble(l1,l2):
    st=''
    while len(l1)>0 and len(l2)>0:
        st=st+str(l1[0])+str(l2[0])
        if len(l1)>=2:
            st=st+'+'
        l1.pop(0),l2.pop(0)
    return st

w=list(combinations(x,len(y)))
for i in range(len(w)):
    print(assemble(list(w[0]),['first','second','third']))
    w.pop(0) """

