# Implement binary search on sorted list.

def binary_search(a,x):
    low,high = 0,len(a)-1
    
    while low<=high:
        mid = (low+high)//2
        if a[mid]==x:
            return mid
        if a[mid]<x:
            low = mid+1
        else:
            high = mid-1
        return -1
    
if __name__ =="__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print(binary_search(arr,10),binary_search(arr,4))
            