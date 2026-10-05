class item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight

def fractional_knapsack(arr,w):
    arr.sort(key=lambda x:x.value/x.weight,reverse=True)
    current_weight=0
    total_profit=0

    for i in range(len(arr)):
        if current_weight+arr[i].weight<=w:
            current_weight+=arr[i].weight
            total_profit+=arr[i].value
        else:
            remaining=w-current_weight
            fraction=remaining*(arr[i].value/arr[i].weight)
            total_profit+=fraction
            break
    return total_profit

arr=[item(60,10),item(100,50),item(200,50),item(100,20)]
w=90
ans=fractional_knapsack(arr,w)
print(ans)