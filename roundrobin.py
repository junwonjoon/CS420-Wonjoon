import pandas as pd
import streamlit as st
import math



def find_lcm(numbers):
    """
    Find the Least Common Multiple (LCM) of a list of numbers.

    Parameters:
    numbers (list): A list of integers to find the LCM for.

    Returns:
    int: The Least Common Multiple of the input numbers.
    """
    if not numbers:
        return 0
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = (lcm * num) // math.gcd(lcm, num)
    return lcm


def round_robin_scheduler(num_processes, time_quantum, burst_times):
    # Initialize process queue with burst times and process names
    process_queue = [{'Process': f'P{i + 1}', 'Burst Time': burst_times[i], 'Remaining Time': burst_times[i]} for i in
                     range(num_processes)]
    time = 0
    time_states = {f'Time {t}': [''] * num_processes for t in range(sum(burst_times) + 1)}

    # Continue until all processes are completed
    while any(process['Remaining Time'] > 0 for process in process_queue):
        for i, process in enumerate(process_queue):
            # Check if the process has remaining time
            if process['Remaining Time'] > 0:
                # Mark the process as "Ready" at the current time step if it’s about to run
                time_states[f'Time {time}'][i] = 'Ready'

                # Calculate run time for the process (minimum of time quantum or remaining time)
                run_time = min(time_quantum, process['Remaining Time'])

                # Update the status to "Running" for each time unit the process runs
                for t in range(run_time):
                    time_states[f'Time {time + t}'][i] = 'Running'

                # Advance the time and reduce the process's remaining time
                time += run_time
                process['Remaining Time'] -= run_time

                # Check if process is completed or moves to waiting
                if process['Remaining Time'] > 0:
                    time_states[f'Time {time}'][i] = 'Ready'
                else:
                    time_states[f'Time {time}'][i] = 'Completed'

    # Create a DataFrame with process names as rows and time steps as columns
    status_df = pd.DataFrame(time_states, index=[process['Process'] for process in process_queue])

    # Replace all blank entries with "Ready"
    status_df.replace('', 'Ready', inplace=True)

    # Define styling function
    def style_status(val):
        style_running = "color: #418fda"
        style_ready = "color: #aadcee"
        style_complete = "color: #4631ac"

        if val == "Running":
            return style_running
        elif val == "Ready":
            return style_ready
        elif val == "Completed":
            return style_complete
        elif val == "Waiting":
            return "color: gray"
        else:
            return ""  # No styling for other cases

    # Apply the styling
    styled_df = status_df.style.applymap(style_status)

    return styled_df
process_times = []
st.header('Round Robin Scheduler')
st.subheader("Select number of processes to run")
num_processes = st.slider('Number of processes', min_value=1, max_value=10)
st.subheader("Select the time quantum")
time_quantum = st.slider('Time units', min_value=1, max_value=10)
st.subheader("Select the values for each processes")
for i in range(num_processes):
    num = st.number_input(f"Pick a time for Process {i + 1}", min_value=1, max_value=time_quantum + 10)
    process_times.append(num)
result = round_robin_scheduler(num_processes, time_quantum, process_times)
st.subheader("The visualization of the Round Robin Scheduler")
st.write(result)
