def swap(arr,i,j): 
    arr[i],arr[j] = arr[j],arr[i] 

def partiton(arr,low,high): 
    mid = (low+high)//2 
    if arr[low] > arr[high]: 
        swap(arr,low,high)
    if arr[mid] < arr[low]: 
        swap(arr,mid,low)
    if arr[mid] > arr[high]: 
        swap(arr,high,mid) 
    return partorg(arr,low,high)     
def partorg(arr,low,high): 
    i = low -1 
    pivot = arr[high] 
    for x in range(low,high): 
        if arr[x]<= pivot: 
            i = i + 1 
            arr[i],arr[x] = arr[x],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]  
    return i+1 
def mediansort(arr,low,high): 
    if low < high: 
        pivot = partiton(arr,low,high) 
        mediansort(arr,low,pivot-1) 
        mediansort(arr,pivot+1,high)  

     