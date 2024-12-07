### For CS420, Made By Wonjoon Jun 
(Please report any problems to junwonjoon41@gmail.com)
# Interactive Demonstration of Schedulers
## Streamlit Page
Click [here](https://cs420-scheduler-demo.streamlit.app/) for the web view of this repository.  

## Introduction
Welcome to the **Interactive Demonstration of Schedulers**! This project is designed to provide an engaging and intuitive way to learn about various CPU scheduling algorithms used in operating systems. From basic scheduling methods to advanced real-time algorithms, this tool enables you to visualize, experiment, and compare their behaviors.

## Features
- **Interactive Visualizations:** See how processes are scheduled in real-time.
- **Customizable Inputs:** Customize input data such as number of processes, execution times, and time quantum.
- **Algorithm Comparison:** Observe and analyze the differences in performance between scheduling techniques.

## Algorithms Covered
1. **[Round Robin (RR) Scheduling](https://cs420-scheduler-demo.streamlit.app/Round_Robin_Scheduling_%F0%9F%94%84):** Time slices are shared equally among processes.
2. **[Rate Monotonic Scheduling (RMS)](https://cs420-scheduler-demo.streamlit.app/Rate_Monotonic_Scheduling_%E2%8F%B1):** A real-time scheduling algorithm where processes with shorter periods are assigned higher priorities.
3. **[Experimental Round Robin Scheduling](https://cs420-scheduler-demo.streamlit.app/Experimental_Round_Robin_%F0%9F%94%81):** Who knows what will happen, if we add individual time quantum for each process. 



## Installation
To run this project locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/junwonjoon/CS420-Wonjoon/
   ```
2. Navigate to the project directory:
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program using terminal:
   ```bash
   streamlit run Welcome_Page_👋.py
   ```
5. Open your browser and navigate to `http://localhost:(specified address by terminal/console)`.
6. Input process parameters, select an algorithm, and view the scheduling results in real-time.


