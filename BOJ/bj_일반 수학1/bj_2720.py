from decimal import Decimal
C = int(input())
for _ in range(C) :
    Q, D, N, P = 0, 0, 0, 0
    T = int(input())/100
    while T != 0 :
        if (T >= 0.25) :
            Q += 1
            T = float(Decimal(str(T)) - Decimal('0.25'))
            # print("Q : " , Q, T)
        elif (T < 0.25 and T >= 0.1) :
            D += 1
            T = float(Decimal(str(T)) - Decimal('0.1'))
            # print("D : " , D, T)
        elif (T < 0.1 and T >= 0.05) :
            N += 1
            T = float(Decimal(str(T)) - Decimal('0.05'))
            # print("N : " , N, T)
        else :
            P += 1
            T = float(Decimal(str(T)) - Decimal('0.01'))
            # print("P : " , P, T)
    print(Q, D, N, P)