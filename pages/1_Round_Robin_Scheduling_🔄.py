import pandas as pd
import streamlit as st
from classLib import Process, style_status
from random import randint

st.set_page_config(
    page_title="Round Robin Scheduling",
    page_icon="🔄",
)
st.sidebar.subheader("Select the headers above to explore different pages")


def round_robin_scheduler(num_processes, time_quantum, execution_times, extend=False):
    # Initialize process queue with burst times and process names
    processes_list = []
    complete = 0
    for i in range(num_processes):
        index = i + 1
        processes_list.append(Process(index, execution_times[i], execution_times[i]))
    timer, process_index, time_ran, cycle_count = 0, 0, 0, 0
    condition = True
    while condition:
        timer += 1
        time_ran += 1
        processes_list[process_index].decrement_time_left(1)
        processes_list[process_index].update_complete()
        process_title = f"Time {timer}"
        for process in processes_list:
            if process != processes_list[process_index]:
                process.update_status({f'{process_title}': 'Ready\t'})
            else:
                message = 'Ran and Got Completed' if process.get_time_left() == 0 else 'Running\t'
                process.update_status({f'{process_title}': message})
        if time_ran == time_quantum or processes_list[process_index].time_left == 0:
            if processes_list[process_index].time_left == 0:
                processes_list[process_index].time_left = processes_list[process_index].get_execution_time()
            process_index += 1
            process_index %= num_processes
            cycle_count += 1
            time_ran = 0
        if not extend:
            condition = False in [x.get_complete() for x in processes_list] or process_index != 0
        else:
            condition = cycle_count != 100
    data = [x.get_status() for x in processes_list]
    flattened_data = [dict(item for d in row for item in d.items()) for row in data]
    status_df = pd.DataFrame(flattened_data)
    status_df.insert(0, 'Processes', [f'Process {i + 1}' for i in range(num_processes)])
    styled_df = status_df.style.map(style_status)
    return styled_df


processTimes = []
st.session_state.setdefault("num_processes_RR", 3)
st.session_state.setdefault("time_quantum_RR", 4)
st.session_state.setdefault("process_time_RR", [randint(1, 5) for _ in range(10)])
st.title('Round Robin (RR) Scheduling Demonstration')
st.subheader("Step 1: Select number of processes to run")
numProcesses = st.slider('Number of processes', min_value=1, max_value=10, value=st.session_state.num_processes_RR)
st.subheader("Step 2: Select the time quantum")
timeQuantum = st.slider('Time units', min_value=1, max_value=10, value=st.session_state.time_quantum_RR)
pick_message = "Step 3: Select the execution time for each processes" if len(
    processTimes) > 1 else "Step 3: Select the execution time for each process"
st.subheader(f"{pick_message}")
for i in range(numProcesses):
    num = st.number_input(f"Pick a time for Process {i + 1}", min_value=1, max_value=99,
                          value=st.session_state.process_time_RR[i])
    processTimes.append(num)
st.divider()
st.subheader("Step 4: Run Demonstration")
next_button = False
if st.button("Run Demonstration"):
    st.session_state["num_processes_RR"] = numProcesses
    st.session_state["time_quantum_RR"] = timeQuantum
    for i in range(len(processTimes)):
        st.session_state["process_time_RR"][i] = processTimes[i]
    result = round_robin_scheduler(numProcesses, timeQuantum, processTimes)
    st.write(
        "The table below shows the timeline for each process. "
        "Status values include:\n"
        "- **Running**: The process is currently executing.\n"
        "- **Ready**: The process is waiting for its turn to execute.\n"
        "- **Ran and Got Completed**: The process has completed its execution for this period."
    )
    st.subheader("The visualization of the Round Robin Scheduler")
    st.write(result)
    next_button = True
    st.markdown("""
    ### Extending to next 100 cycles
    #### The visualization of the next 100 cycles
    """)
    result_extended = round_robin_scheduler(numProcesses, timeQuantum, processTimes, extend=True)
    st.write(result_extended)
