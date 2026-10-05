def partition(arr,start,end):
    idx=start-1
    pivot=arr[end]

    for j in range(start,end):
        if(arr[j]<=pivot):
            idx+=1
            arr[j],arr[idx]=arr[idx],arr[j]

    idx+=1
    arr[end],arr[idx]=arr[idx],arr[end]
    return idx


def quick_sort(arr,start,end):
    if start<end:
        pivot_index=partition(arr,start,end)
        quick_sort(arr,start,pivot_index-1)
        quick_sort(arr,pivot_index+1,end)
arr=[10,16,8,12,15,6,3,9,5]
quick_sort(arr,0,len(arr)-1)
print(arr)

