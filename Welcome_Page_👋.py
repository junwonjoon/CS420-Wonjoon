import streamlit as st

url_round_robin = "https://cs420-scheduler-demo.streamlit.app/Round_Robin_Scheduling_%F0%9F%94%84"
url_RMS = "https://cs420-scheduler-demo.streamlit.app/Rate_Monotonic_Scheduling_%E2%8F%B1"
url_RR_experimental = "https://cs420-scheduler-demo.streamlit.app/Experimental_Round_Robin_%F0%9F%94%81"

st.set_page_config(
    page_title="Welcome Page",
    page_icon="👋",
)
st.sidebar.subheader("Select the headers above to explore different pages")
st.markdown(
    f"""
# Welcome to This Page

## Overview
This project provides an engaging, hands-on demonstration of various CPU scheduling algorithms, crucial for operating systems. Learn how schedulers determine the order in which processes execute to maximize efficiency and fairness. 

## Topics Covered
- **[Round Robin (RR) Scheduling]({url_round_robin}):** Time slices are shared equally among processes.
- **[Rate Monotonic Scheduling (RMS)]({url_RMS}):** A real-time scheduling algorithm where processes with shorter periods are assigned higher priorities.
- **[Experimental Round Robin Scheduling]({url_RR_experimental}):** Who knows what will happen, if we add individual time quantum for each process? 
##### To navigate please use the side bar on the *left* to view different scheduling algorithms.

## Interactive Features
- Visualize the scheduling process in real-time.
- Customize input data such as number of processes, execution times, and time quantum.
- Compare results between different scheduling algorithms.

## Learning Outcomes
- Understand the trade-offs and use cases for different scheduling techniques.
- Explore how schedulers impact system performance and user experience.

### GitHub Repository
Click [here](https://github.com/junwonjoon/CS420-Wonjoon) to view the repository.

#### Author
Wonjoon Jun

#### With Special Thanks to
Professor King
""")
