arr=list(map(int,input("Array:").split()))
target=int(input("Target:"))
n=len(arr)
found=-1
for i in range(n):
    if arr[i]==target:
        found=i
        break

print("Element found at index:",found)