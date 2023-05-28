# Jobs, Profit, Slot
profit = [15,27,10,100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 
profitNJobs = list(zip(profit,jobs,deadline))                                        #ZIP function is used to combine 3 lists together
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)            #lambda 0 says that sorting should be based on first element and reverse meand descending order
slot = []                                            
for _ in range(len(jobs)):                                                   #creating slot named list of length of length of jobs and initializing all with 0
    slot.append(0)

profit = 0                                  #created profit variable and initialized to 0
ans = []                                    #created ans named list and initialized with null

for i in range(len(jobs)):                 
    ans.append('null')                     

for i in range(len(jobs)):                 #loop iterated over range of indices of jobs and var I represents current index
        job = profitNJobs[i]               
        #check if slot is occupied
        for j in range(job[2], 0, -1):        #finds the first available slot (in reverse order) for a job and schedules the job in that slot. 
                                              #It updates the ans list with the scheduled job's name, adds the job's profit to the total profit, 
                                              #and marks the slot as occupied. The code breaks out of the loop once a suitable slot is found.
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Jobs scheduled buddy:",ans[1:])
print(profit)




"""
The job scheduling problem with deadlines is a variant of the basic job scheduling problem where each job has an associated deadline,
 and the objective is to maximize the total profit by scheduling the jobs within their deadlines. 
In this problem, each job has a profit and a deadline, and the goal is to find a schedule that maximizes the total profit without missing any deadlines.

The greedy search algorithm for the job scheduling problem with deadlines can be implemented using the following steps:

Sort the jobs in descending order of their profits.

This step ensures that higher-profit jobs are considered first during the scheduling process.
Initialize an empty schedule and a set of available time slots.

The schedule will store the assigned jobs, and the available time slots will help determine where each job should be scheduled.
Iterate through the sorted jobs and assign each job to the earliest available time slot that does not exceed its deadline.

For each job, check the available time slots starting from its deadline down to 1.
If an available time slot is found, assign the job to that slot in the schedule and mark the slot as occupied.
If no available time slot is found, skip the job (or optionally, assign it to a penalty slot if penalties are allowed).
Calculate the total profit of the scheduled jobs.

Return the resulting schedule and the total profit.

The greedy search algorithm prioritizes jobs with higher profits and assigns them to the earliest available time slots that satisfy their deadlines. 
This approach aims to maximize the total profit while ensuring that jobs are completed within their deadlines.

It's important to note that this greedy algorithm may not always find an optimal solution. 
There can be cases where an optimal solution requires a different scheduling order than the one obtained by the greedy approach.
To guarantee an optimal solution, other optimization techniques such as dynamic programming or backtracking can be used, but they may come with higher computational complexity.
"""
