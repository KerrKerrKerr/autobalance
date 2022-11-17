if __name__ == "__main__":
    from numba import njit,jit
    n = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    e_names = [0,"H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl",'Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe']      
    m_masses = [0,1,4,7,9,11,12,14,16,19,20,23,24,27,28,31,32,35.5,40,39,40,45,48,51,52,55,56,59,59,63.5,65]

    def k(y,n): #takes 2 args,can be used with (n)jit but thats worse then without. first: string where koef needs to be extracted. second: tuple from '0' to '9' with name n as default
        a=""
        while (len(y)>=1) and (y[0] in n):
            a+=y[0]
            y=y[1:]
        return a,y #1:extracted koef as integer 2:string without koef

    def braces_find(x): #returns indexes of braces as a list. first returns '(', second ')'
        b_opening_i,b_closing_i = [],[]
        for i in range(len(x)):
            if (x[i] == '('):
                b_opening_i.append(i)
            if (x[i] == ')'):
                b_closing_i.append(i)  
        if len(b_opening_i)==0 and len(b_closing_i)==0:          
            return
        elif len(b_opening_i) != len(b_closing_i):
            print("critical error: brace wasn`t closed or opened")
            return "critical error: brace wasn`t closed or opened",None
        else:
            if len(b_closing_i) >=2:
                b_closing_i.reverse()
            return b_opening_i,b_closing_i
        
    def moles(x): #main function
        koef,x = k(x,n)
        koef = int(koef)
        print(x,koef)
        print(braces_find(x))
        for i in enumerate(x):
            

            k(x,n)

    print(moles("123(Ca(NO3)2)"))
