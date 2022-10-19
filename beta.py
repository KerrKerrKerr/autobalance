from fun import *
from itertools import combinations
inp=str(input())
inp = inp.split('=>')
w=list(combinations(nn,len(('+'.join(inp).split('+')))))
i1, i2 = inp[0], inp[1]
i1_2, i2_2 = i1.split('+'), i2.split('+')
print(i1_2)
print(k_delete(i1_2))
for i in range(len(w)):
    w0=list(w[0])
    print(assemble(w0,(k_delete('+'.join(inp).split('+')).copy())))
    w.pop(0)