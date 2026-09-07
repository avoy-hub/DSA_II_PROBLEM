def merge(arr, start, middle, end):
    left=[]
    right=[]
    i=start
    while i<=middle:
        left.append(arr[i])
        i=i+1

    i=middle+1
    while i<=end:
        right.append(arr[i])
        i=i+1

    i=0
    j=0
    k=start

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1

    while i<len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1

    while j<len(right):
        arr[k]=right[j]
        j=j+1
        k=k+1


    
def merge_sort(arr, start, end):
    if start < end:

        middle = (start + end) // 2

        merge_sort(arr, start, middle)
        merge_sort(arr, middle + 1, end)

        merge(arr, start, middle, end)


arr = [1, 3, 2, 8, 4, 5, 7, 6]

merge_sort(arr, 0, len(arr) - 1)

print(arr)