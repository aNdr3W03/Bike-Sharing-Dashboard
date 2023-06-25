# Bike Sharing Dashboard

Streamlit Cloud: <a href='https://bike-sharing.streamlit.app' target='_blank' title='Bike Sharing Dashboard | Streamlit'>Bike Sharing Dashboard</a>

## Preview

https://github.com/aNdr3W03/Bike-Sharing-Dashboard/assets/64983961/77e55eda-49d4-47c5-8486-7a9086ed3eb1

## Description

This project is part of the bike sharing data analysis project to analyze the <a href='https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ' target='_blank' title='Bike-sharing-dataset.zip'>Bike Sharing Dataset</a>. The results of the analysis are then made into the form of data visualization into an interactive dashboard.

## Directory

- `/assets`: stores image and video assets used in this project
- `/dashboard`: contains the file `func.py` which stores the functions needed by the dashboard
- `dataset`: stores data used in the data analysis project
- `README.md`: file that provides information about this GitHub project
- `app.py`: main file to run the dashboard
- `notebook.ipynb`: interactive jupyter notebook files to analyze data
- `requirements.txt`: file that stores information about the libraries used in this project

## Installation

The steps to create your virtual environment from this project is as follows:

1. Clone this Repository
   ```bash
   git clone https://github.com/aNdr3W03/Bike-Sharing-Dashboard.git
   ```

2. Create Python Virtual Environment
   ```bash
   virtualenv venv
   ```

2. Activate the Environment
   ```bash
   venv\Scripts\activate
   ```

4. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Streamlit Dashboard
   ```bash
   streamlit run app.py
   ```

6. Stop the application program by `ctrl + c`.
