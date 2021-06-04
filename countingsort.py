def countingsort(arr,b,k): 
    c = [0]*(k+1)  
    for j in range(len(arr)): 
        c[arr[j]] = c[arr[j]] + 1 
    for x in range(1,len(c)): 
        c[x] = c[x] + c[x-1] 
    for n in arr: 
        b[c[n]-1] = n 
        c[n] =  c[n] - 1 
    return b 
arr = [2,5,3,0,2,3,0,3]  
k = max(arr) 
b = [0]*len(arr) 
print(countingsort(arr,b,k)) 



