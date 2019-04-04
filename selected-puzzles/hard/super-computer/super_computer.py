tasks = []
n = int(input())
for i in range(n):
    start_day, duration = [int(j) for j in input().split()]
    task = (start_day + duration - 1, start_day)  # end day, start day
    tasks.append(task)

tasks.sort()

carry_list = []
carry_list.append(tasks[0])
prev_index = 0
for i in range(1, n):
    task = tasks[i]
    prev_task = tasks[prev_index]
    if task[1] > prev_task[0]:  # check if task doesn't overlap
        carry_list.append(task)
        prev_index = i

print(len(carry_list))
