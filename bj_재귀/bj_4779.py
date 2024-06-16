def cantoa(n) : 
    if n == 0 : 
        s = "-"
        return s
    k = cantoa(n-1) + len(cantoa(n-1)) * " "
    return k + cantoa(n-1)

while(True) :
    try :
        N = int(input())
        print(cantoa(N))
    except :
        break