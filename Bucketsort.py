def insertion(arr): 
    for x in range(1,len(arr)): 
        key = arr[x] 
        y = x -1 
        while y >= 0 and arr[y] > key: 
            arr[y+1] = arr[y] 
            y -= 1 
        arr[y+1] = key #case as more num in array maybe small than key 
    return arr     
def bucketsort(arr): 
    b = [] 
    val = 10 #as number is between [0,1) so using 10 to create a bucket 
    for i in range(len(arr)): 
        b.append([]) #creating a list inisde another list 
    for i in arr: 
        n = int(i * val) #waeyo? cause using ceiling value  
        b[n-1].append(i) #bucket created 
    for i in range(len(arr)): 
        b[i] = insertion(b[i]) 
    result = [] 
    for x in range(len(arr)): #concacting the sorted array
        result = result + b[x] 
    return result    
arr = [0.9, 0.1, 0.6, 0.7, 0.6, 0.3, 0.1]    
print(bucketsort(arr))   
