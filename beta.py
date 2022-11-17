from fun import *
from itertools import product
inp=str(input())
inp = inp.split('=>')
w=list(product(nn,repeat=len(('+'.join(inp).split('+')))))
i1, i2 = inp[0], inp[1]
i1_2, i2_2 = i1.split('+'), i2.split('+')
for i in range(len(w)):
    w0=list(w[0])
    var=assemble(w0,(k_delete(smt_new(inp))))
    var=var.split('=>')
    v1,v2=var[0],var[1]
    v1,v2=v1.split('+'),v2.split('+')
    if second_check(v1)==second_check(v2):
        print(f"{var[0]} => {var[1]}")
        break
    w.pop(0)