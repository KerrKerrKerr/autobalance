#from dfg import main
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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
