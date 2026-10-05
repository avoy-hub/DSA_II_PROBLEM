class Job:
    def __init__(self,profit,deadline,id):
        self.profit=profit
        self.deadline=deadline
        self.id=id
def job_scheduling(profit,deadline):
    jobs=[]
    index=1
    for x,y in zip(profit,deadline):
        jobs.append(Job(x,y,index))
        index+=1
    jobs.sort(key=lambda x:x.profit,reverse=True)
    mx_deadline=max(deadline)
    mx_profit=0
    slot=[0]*(mx_deadline+1)
    for job in jobs:
        for t in range(job.deadline,0,-1):
            if slot[t]==0:
                mx_profit+=job.profit
                slot[t]=job.id
                break
    return mx_profit,slot[1:]
profit=[25,15,30,20,12,35,5]
deadline=[4,3,4,2,1,3,2]
profit,schedule=job_scheduling(profit,deadline)
print("Maximum profit:",profit)
print("Schedule:",schedule)
