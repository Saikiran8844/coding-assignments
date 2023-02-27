def job_selection(n, jobs):
    jobs.sort(key=lambda x: x[1])  # sort by end time
    prev_end = 0
    earnings = 0
    selected_jobs = []
    for job in jobs:
        start, end, profit = job
        if start >= prev_end:
            selected_jobs.append(job)
            prev_end = end
            earnings += profit
    remaining_jobs = n - len(selected_jobs)+1
    remaining_earnings = sum(job[2]
                             for job in jobs if job in selected_jobs)
    return remaining_jobs, remaining_earnings


if __name__ == '__main__':
    n = int(input("Enter the number of Jobs: "))
    jobs = []
    print("Enter job start time (in HHMM 24HRS format): \n Enter job end time (in HHMM 24HRS format): \n Enter job earnings:")
    for i in range(n):
        # append jobs and profit list oon each iterations
        jobs.append(list(map(int, input().split())))

    remaining_jobs, remaining_earnings = job_selection(n, jobs)

    print("The number of tasks and earnings available for others")
    print(f"Task: {remaining_jobs}")
    print(f"Earnings: {remaining_earnings}")
