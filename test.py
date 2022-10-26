n=[i for i in range(0,10)]

def perf(inp):
    inp=inp.copy()
    if inp[0] in n:
        k=0
        while inp[0]in n:
            k+=inp[0]
            inp=inp.replace(inp[0],'',1)
    
