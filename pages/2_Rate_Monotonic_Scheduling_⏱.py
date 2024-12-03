import pandas as pd
import streamlit as st
import heapq
from classLib import style_status
from random import randint

st.set_page_config(
    page_title="Rate Monotonic Scheduling",
    page_icon="⏱️",
)
st.sidebar.subheader("Select the headers above to explore different pages")


# The basis of RMS was obtained from https://github.com/floo-bar/Rate-Monotonic-Scheduling/blob/master/rate_mono.py
class Task:
    def __init__(self, name, period, execution_time):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.deadline = period
        self.remaining_time = execution_time

    def __lt__(self, other):
        return self.period < other.period


def rms_scheduler(tasks, time_limit=150):
    current_time = 0
    task_queue = []
    data_time_list = []
    while tasks:
        for task in tasks:
            if current_time % task.period == 0:
                task.remaining_time = task.execution_time
                task.deadline = current_time + task.period
                heapq.heappush(task_queue, task)

        if task_queue:
            current_task = heapq.heappop(task_queue)
            data_time_list.append([current_time, current_task.name])
            current_time += 1
            current_task.remaining_time -= 1
            if current_task.remaining_time != 0:
                heapq.heappush(task_queue, current_task)
        else:
            current_time += 1
        if current_time > time_limit:
            break
    return data_time_list


def generate_RMS_df(tasks, time_limit=150):
    data = rms_scheduler(tasks, time_limit)
    processes_list = {"Time 0": ["Ready" for _ in range(len(tasks))]}
    RMS_df = pd.DataFrame(processes_list)
    time_counter = 1
    for time in range(int(data[-1][0]) + 1):
        df_elem = ["Ready" for _ in range(len(tasks))]
        for i in range(len(tasks)):
            for elem in data:
                if str(i+1) in elem[1] and time == elem[0]:
                    df_elem[i] = "Running"
        RMS_df[f'Time {time+1}'] = df_elem
        time_counter += 1
    for i in range(len(tasks)):
        copy_of_row = RMS_df.iloc[i].copy()
        counter = -1
        for elem in RMS_df.iloc[i]:
            counter += 1
            if elem != "Running":
                copy_of_row[counter] = "Ready"
            else:
                break
        RMS_df.iloc[i] = copy_of_row
    RMS_df.insert(0, 'Processes', [f'Process {i + 1}' for i in range(len(tasks))])
    styled_df = RMS_df.style.map(style_status)
    return styled_df


st.session_state.setdefault("num_processes_RMS", 3)
st.session_state.setdefault("max_range_RMS", 150)
st.session_state.setdefault("list_of_execution_times", [randint(1, 2) for _ in range(10)])
st.session_state.setdefault("list_of_periods", [randint(3, 6) for _ in range(10)])
st.title("Rate Monotonic Scheduling (RMS) Demonstration")
st.subheader("Step 1: Select the Number of Processes")
numProcesses = st.slider("Choose the number of processes you want to schedule:", min_value=1,
                         max_value=10,
                         value=st.session_state.num_processes_RMS)

st.subheader("Step 2: Define Process Parameters")
st.write(
    "For each process, set the **execution time** (time needed to complete) and "
    "**period** (frequency of execution)."
)

process_execution_times = []
periods = []
st.markdown(f"#### Step 2.0: Choose the Time Range for the Scheduling Demonstration")
max_display_time_range = st.number_input(f"Choose a Time Range", min_value=100, max_value=1500,
                                         value=st.session_state.max_range_RMS)
for i in range(numProcesses):
    st.markdown(f"#### Step 2.{i + 1}: Choose Values for Process {i + 1}")
    # Time budget for process
    process_execution_time = st.number_input(f"Process {i + 1}: Enter execution time (time budget in units):",
                                             min_value=1,
                                             max_value=99,
                                             value=st.session_state.list_of_execution_times[i]
                                             )
    period = st.number_input(f"Process {i + 1}: Enter period (frequency in units):",
                             min_value=1,
                             max_value=99,
                             value=st.session_state.list_of_periods[i]
                             )
    if process_execution_time >= period:
        st.error("Execution time cannot be greater or equal to the period.")
        exit()
    process_execution_times.append(process_execution_time)
    periods.append(period)
list_of_utilization = [process_execution_times[i] / periods[i] for i in range(len(periods))]
st.write(f"Current Utilization: {sum(list_of_utilization) * 100}%")
if sum(list_of_utilization) > 1:
    st.error("CPU utilization cannot be greater than 100%")
    exit()

st.divider()
st.subheader("Step 3: Run the Scheduler")
st.write("Click the button below to visualize the scheduling timeline for your processes:")
if st.button("Run Scheduler"):
    st.session_state["num_processes_RMS"] = numProcesses
    st.session_state["max_range_RMS"] = max_display_time_range
    for i in range(numProcesses):
        st.session_state["list_of_execution_times"][i] = process_execution_times[i]
        st.session_state["list_of_periods"][i] = periods[i]
    st.subheader("Scheduling Timeline")
    st.write(
        "The table below shows the timeline for each process. "
        "Status values include:\n"
        "- **Running**: The process is currently executing.\n"
        "- **Ready**: The process is waiting for its turn to execute.\n"
        "- **Waiting**: The process is waiting for its next period.\n"
    )
    tasks = [Task(f'Task {i + 1}', periods[i], process_execution_times[i]) for i in range(numProcesses)]
    RMS_df = generate_RMS_df(tasks, max_display_time_range - 1)
    st.write(RMS_df)
