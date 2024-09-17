class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def sjf_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    # Initialize variables
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    # Execute processes
    for i, process in enumerate(processes):
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        waiting_time = current_time - process.arrival_time
        turnaround_time = waiting_time + process.burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        print(f"Process {process.name}:")
        print(f"  Arrival Time: {process.arrival_time}")
        print(f"  Burst Time: {process.burst_time}")
        print(f"  Waiting Time: {waiting_time}")
        print(f"  Turnaround Time: {turnaround_time}")
        print(f"  Execution Time: {current_time}")
        print()

        current_time += process.burst_time

    print(f"Average Waiting Time: {total_waiting_time / len(processes)}")
    print(f"Average Turnaround Time: {total_turnaround_time / len(processes)}")

# Example usage:
processes = [
    Process("P1", 0, 5),
    Process("P2", 2, 3),
    Process("P3", 4, 8),
    Process("P4", 6, 2)
]

sjf_scheduling(processes)