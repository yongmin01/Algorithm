[A, B, V] = [int(x) for x in input().split()]
now = 0
day = 1
mok = V//(A-B)
if V % (A-B) == 0 :
    if (A-B) * (mok-1) + A < V :
        print("case 1")
        print(mok)
    else :
        while (A-B) * mok < V :
            mok -= 1
        print("case 2")
        print(mok)
            
else :
    print("case 3")
    print(V//(A-B)+1)
