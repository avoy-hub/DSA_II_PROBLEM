x,y,z="Apple","banana","cherry"

print(x)
print(y)
print(z)


#multiple return values
def calculator(a,b):
    sum=a+b
    diff=a-b
    return sum,diff

result=calculator(5,10)
print(result)


a,b,c=map(int,input().split())
sum=a+b+c
print(sum)