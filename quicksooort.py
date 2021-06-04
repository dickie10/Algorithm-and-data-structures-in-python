import random  
import sys 
sys.setrecursionlimit(10**6)
def part(arr,low,high): 
    i = low -1 
    pivot = arr[high] 
    for x in range(low,high): 
        if arr[x]<= pivot: 
            i = i + 1 
            arr[i],arr[x] = arr[x],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]  
    return i+1 


def quicksort(arr,low,high): 
    if len(arr) == 1 : 
        return arr 
    if low < high: 
        q = part(arr,low,high)
        quicksort(arr,low,q-1) 
        quicksort(arr,q+1,high)  

arr = [10,20,50,40,100,1000,11] 
quicksort(arr,0,len(arr)-1) 
print(arr)