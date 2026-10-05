a1=[2,6,8,1,4]
a2=[4,2,7,1,2,3]
i=0
j=0
count=0

a1.sort()
a2.sort()

while i<len(a1) and j<len(a2):
    if a1[i]<=a2[j]:
        count+=1
        i+=1
    else:
        j+=1

print(count)
