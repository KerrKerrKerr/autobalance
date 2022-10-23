from fun import *
from itertools import combinations_with_replacement
from test2 import p_
inp=str(input())
inp = inp.split('=>')
w=list(combinations_with_replacement(nn,len(('+'.join(inp).split('+')))))
w=p_(w)
i1, i2 = inp[0], inp[1]
i1_2, i2_2 = i1.split('+'), i2.split('+')
for i in range(len(w)):
    w0=list(w[0])
    print(var:=assemble(w0,(k_delete(smt_new(inp)))),':checked')
    var=var.split('=>')
    v1,v2=var[0],var[1]
    v1,v2=v1.split('+'),v2.split('+')
    if second_check(v1)==second_check(v2):
        print('found one')
        break
    w.pop(0)