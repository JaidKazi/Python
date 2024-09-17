import heapq

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.start_time = None
    
    # Define comparison for heap operations based on remaining burst time
    def __lt__(self, other):
        return self.remaining_burst_time < other.remaining_burst_time

def srtf_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    # Initialize variables
    current_time = 0
    completed_processes = []
    waiting_time_dict = {p.name: 0 for p in processes}
    turnaround_time_dict = {p.name: 0 for p in processes}
    
    # Min-heap for processes based on remaining burst time
    min_heap = []
    process_index = 0
    total_processes = len(processes)
    gantt_chart = []
    last_process = None

    while len(completed_processes) < total_processes:
        # Add new arrivals to the min-heap
        while process_index < total_processes and processes[process_index].arrival_time <= current_time:
            heapq.heappush(min_heap, processes[process_index])
            process_index += 1
        
        if min_heap:
            # Get the process with the shortest remaining time
            current_process = heapq.heappop(min_heap)
            
            # If the process was preempted, add it back to the heap
            if last_process and last_process != current_process:
                heapq.heappush(min_heap, last_process)
            
            if current_process.start_time is None:
                current_process.start_time = current_time

            gantt_chart.append((current_time, current_process.name))
            
            # Process the current process for one unit of time
            current_time += 1
            current_process.remaining_burst_time -= 1

            if current_process.remaining_burst_time == 0:
                # Calculate waiting time and turnaround time
                turnaround_time = current_time - current_process.arrival_time
                waiting_time = turnaround_time - current_process.burst_time
                turnaround_time_dict[current_process.name] = turnaround_time
                waiting_time_dict[current_process.name] = waiting_time
                completed_processes.append(current_process)
                last_process = None
            else:
                last_process = current_process
        else:
            # No process is currently running, move time forward
            current_time += 1

    # Print the Gantt chart
    print("Gantt Chart:")
    prev_time = 0
    for start_time, proc_name in gantt_chart:
        if start_time != prev_time:
            print(f"{prev_time}-{start_time}: {proc_name}", end=" ")
        prev_time = start_time
    if prev_time != current_time:
        print(f"{prev_time}-{current_time}: {last_process.name}")
    print()

    # Print execution details for each process
    for proc in processes:
        print(f"Process {proc.name}:")
        print(f"  Arrival Time: {proc.arrival_time}")
        print(f"  Burst Time: {proc.burst_time}")
        print(f"  Waiting Time: {waiting_time_dict[proc.name]}")
        print(f"  Turnaround Time: {turnaround_time_dict[proc.name]}")
        print(f"  Execution Time: {proc.start_time} to {proc.start_time + proc.burst_time}")
        print()

    # Calculate and print average waiting time and turnaround time
    average_waiting_time = sum(waiting_time_dict.values()) / total_processes
    average_turnaround_time = sum(turnaround_time_dict.values()) / total_processes
    print(f"Average Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

# Example usage:
processes = [
    Process("P1", 0, 5),
    Process("P2", 2, 3),
    Process("P3", 4, 8),
    Process("P4", 6, 2)
]

srtf_scheduling(processes)
