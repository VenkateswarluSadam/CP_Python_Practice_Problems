ar,n=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],12
                                            #Trapping Water Problem O(n/2)
l_max, r_max = 0, n-1

l, r = ar[0], ar[n-1]

for i in range(len(ar)):
    if i>=n-1-i:
        break
    if ar[i]>l:
        l_max=i
        l=ar[i]
    if ar[n-1-i]>r:
        r_max=n-1-i
        r=ar[n-1-i]
ans=0 
print(ar[l_max],ar[r_max])
temp=min((ar[l_max],ar[r_max]))

for i in range(l_max,r_max):
    ans+=abs(temp-ar[i])
    print(ans)
    
print(ans)    
