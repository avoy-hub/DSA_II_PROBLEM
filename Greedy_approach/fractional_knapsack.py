class item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight

arr=[item(60,10),item(100,50),item(200,50),item(100,20)]
w=90
arr.sort(key=lambda x:x.value/x.weight,reverse=True)
current_weight=0
total_profit=0

for i in range(0,len(arr)):
    if current_weight+arr[i].weight<=w:
        current_weight+=arr[i].weight
        total_profit+=arr[i].value
    else:
        remaining_weight=w-current_weight
        fractional_profit=remaining_weight*(arr[i].value/arr[i].weight)
        total_profit+=fractional_profit

print(total_profit)