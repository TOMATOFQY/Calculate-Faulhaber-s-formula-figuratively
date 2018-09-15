import numpy as np
import time

funcList = []
funcList.append(lambda n: n)
funcList.append(lambda n: n*(n+1)/2)
funcList.append(lambda n: n*(n+1)*(n+1/2)/3)

a = np.mat([[1,1],[3,5]])
C = [[],[]]

def generateB(n,notperfectfunc):
    b = []
    sum = 0
    for i in range(n+1)[1:]:
        sum += i ** n
        b.append(sum - notperfectfunc(i) )
    b.remove(b[0])
    b = np.mat(b).T
    return b

def generateNotperfectFunc(n):
    def func(x):
        return funcList[n-1](x)*( x + 1/n)*n/(n+1)
    return func

def generatePerfectFunc(oldfun,r):
    def func(x):
        result = oldfun(x)
        for i,c in enumerate(r):
            result += funcList[i+1](x-1) * c 
        return result
    return func

def displayfun(n):
    print("S%d(n) = [(1+%d*n)*S%d(n)]/(%d)" % (n,n,n-1,n+1),end='')
    for i in range(n-1):    
        if C[n-1] != []: 
            print(" + %.3f*S%d"%(C[n-1][i],i+1),end='')
    print()
    
if __name__ == '__main__':
    for n in range(20)[3:]:
        t = time.time()

        #caculate b
        b = generateB(n,generateNotperfectFunc(n))
        r = np.linalg.solve(a,b)

        #update C
        c = []
        for i in r:
            c.append(float(i))
        C.append(c)

        #update funcList
        perfectfun = generatePerfectFunc(generateNotperfectFunc(n),c)
        funcList.append(perfectfun)

        #update A
        row = []
        for i in range(n)[1:]:
            row.append(funcList[i](n))
        a = np.row_stack((a,row))
        colum = []
        for i in range(n+1)[1:]:
            colum.append(funcList[n](i))
        a = np.column_stack((a,colum))

        print(n,time.time()-t)
        displayfun(n)
        print()
        # diaplayfun(n)