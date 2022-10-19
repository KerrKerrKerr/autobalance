from fun import *
inp=str(input()).split('=>')
i1, i2 = inp[0], inp[1]
i1, i2 = i1.split('+'), i2.split('+')

print(second_check(i1)==second_check(i2))