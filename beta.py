from fun import *
from itertools import combinations
inp=str(input())
w=list(combinations(nn,len((''.join('+').split('+')))))
inp = inp.split('=>')
i1, i2 = inp[0], inp[1]
i1_2, i2_2 = i1.split('+'), i2.split('+')
print(i1,i1_2)
print(k_delete(i1_2))
""" for i in range(len(w)):
    print(assemble(w[0],(k_delete(inp))))
    w.pop(0) """