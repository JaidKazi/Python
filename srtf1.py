# Define the processes with their arrival times (AT) and burst times (BT)
processes = [
    {"name": "P1", "AT": 0, "BT": 7},
    {"name": "P2", "AT": 2, "BT": 4},
    {"name": "P3", "AT": 4, "BT": 1},
    {"name": "P4", "AT": 5, "BT": 4}
]

# Sort the processes by their arrival times
processes.sort(key=lambda x: x["AT"])

# Initialize variables to store the waiting time, turnaround time, and execution time
WT = [0] * len(processes)
TAT = [0] * len(processes)
execution_time = 0

# Create a Gantt chart to visualize the process execution
gantt_chart = []

# Iterate through the processes
for i in range(len(processes)):
    # Find the process with the shortest remaining time
    min_BT = float("inf")
    min_index = -1
    for j in range(i, len(processes)):
        if processes[j]["BT"] < min_BT:
            min_BT = processes[j]["BT"]
            min_index = j

    # Swap the processes if necessary
    if min_index != i:
        processes[i], processes[min_index] = processes[min_index], processes[i]

    # Update the waiting time, turnaround time, and execution time
    WT[i] = execution_time - processes[i]["AT"]
    TAT[i] = WT[i] + processes[i]["BT"]
    execution_time += processes[i]["BT"]

    # Add the process to the Gantt chart
    gantt_chart.append((processes[i]["name"], execution_time))

# Print the results
print("Process\tWT\tTAT\tExecution Time")
for i in range(len(processes)):
    print(f"{processes[i]['name']}\t{WT[i]}\t{TAT[i]}\t{execution_time}")

print("\nGantt Chart:")
for i in range(len(gantt_chart)):
    print(f"{gantt_chart[i][0]}: {gantt_chart[i][1]}")