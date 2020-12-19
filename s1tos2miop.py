s1 = 'cart'
s2 = 'march'
m,n = len(s1) , len(s2)
dp = []
for i in range(m+1):
    a = []
    for j in range(n+1):
        a.append(0)
    dp.append(a)
        
print(dp)        
    
print("-----------------------")
for i in range(m+1):
    for j in range(n+1):
        
        if i==0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i 
        elif s1[i-1] == s2[j-1] :
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
        for k in dp:
            print(k)
        print("--------------------------------",i,j)
print(dp[m][n])

    
#insert
#delete
#modify
#we have to convert s1 into s2 with minimum operations
