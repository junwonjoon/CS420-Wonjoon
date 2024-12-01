### For CS420, Made By Wonjoon Jun
# Interactive Demonstration of Schedulers

## Introduction
Welcome to the **Interactive Demonstration of Schedulers**! This project is designed to provide an engaging and intuitive way to learn about various CPU scheduling algorithms used in operating systems. From basic scheduling methods to advanced real-time algorithms, this tool enables you to visualize, experiment, and compare their behaviors.

## Features
- **Interactive Visualizations:** See how processes are scheduled in real-time.
- **Customizable Inputs:** Customize input data such as number of processes, execution times, and time quantum.
- **Algorithm Comparison:** Observe and analyze the differences in performance between scheduling techniques.

## Algorithms Covered
1. **Round Robin (RR):** Time slices are shared equally among processes.
2. **Rate Monotonic Scheduling (RMS):** A real-time scheduling algorithm where processes with shorter periods are assigned higher priorities.


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
   streamlit run Welcome_Page.py
   ```
5. Open your browser and navigate to `http://localhost:3000` (or the specified address).
6. Input process parameters, select an algorithm, and view the scheduling results in real-time.


