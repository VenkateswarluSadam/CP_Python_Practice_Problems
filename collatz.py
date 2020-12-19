def getLength(n):
    if n==1: 
        return 1 
    if n%2==1:
        return 1+getLength(3*n+1)
    else:
        return 1+getLength(n//2)
        
def sol(n):
    mlen =  1 
    for i in range(1,n+1):
        
        l_i = getLength(i)
        
        if l_i > mlen :
            mlen = l_i
            
        #mlen = max(l_i,mlen)
        
    return mlen
    
print(sol(10))
