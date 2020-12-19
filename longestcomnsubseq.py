x = 'aggtab'
y = 'gxtxayb'
m = len(x)
n = len(y)
l = [[0]*(m+2)]*(n+2)

for i in range(m+1):
    for j in range(n+1):
        
        if i==0 or j==0:
            
            l[i][j] = 0
            
        elif x[i-1] == y[j-1]:
            l[i][j] = l[i-1][j-1] + 1
        else:
            l[i][j] = max(l[i-1][j], l[i][j-1])
print(l[m][n])
