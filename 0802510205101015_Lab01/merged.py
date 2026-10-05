arr1=list(map(int,input("Array 1:").split()))
arr2=list(map(int,input("Array 2:").split()))
merged=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        merged.append(arr1[i])
        i=i+1
    else:
        merged.append(arr2[j])
        j=j+1


while i<len(arr1):
    merged.append(arr1[i])
    i=i+1

while j<len(arr2):
    merged.append(arr2[j])
    j=j+1

print("Merged Array:",merged)

