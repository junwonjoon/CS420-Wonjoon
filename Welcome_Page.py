import streamlit as st


st.set_page_config(
    page_title="Welcome Page",
    page_icon="👋",
)
st.sidebar.subheader("Select the headers above to explore different pages")
st.markdown(
    """
# Welcome to My Interactive Demonstration of Schedulers

## Overview
This project provides an engaging, hands-on demonstration of various CPU scheduling algorithms, crucial for operating systems. Learn how schedulers determine the order in which processes execute to maximize efficiency and fairness. 

## Topics Covered
- **[Round Robin (RR)](https://cs420-scheduler-demo.streamlit.app/Round_Robin_Scheduling):** Time slices are shared equally among processes.
- **Rate Monotonic Scheduling (RMS):** A real-time scheduling algorithm where processes with shorter periods are assigned higher priorities.
To navigate please use the side bar on the left to view different scheduling algorithms.

## Interactive Features
- Visualize the scheduling process in real-time.
- Customize input data such as number of processes, execution times, and time quantum.
- Compare results between different scheduling algorithms.

## Learning Outcomes
- Understand the trade-offs and use cases for different scheduling techniques.
- Explore how schedulers impact system performance and user experience.

### GitHub Repository
Click [here](https://github.com/junwonjoon/CS420-Wonjoon) to view the repository.


Dive into the world of schedulers and see how operating systems manage multitasking efficiently!
""")
