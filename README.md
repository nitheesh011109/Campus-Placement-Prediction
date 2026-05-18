# Placement & Salary Prediction System

An end-to-end machine learning project that predicts student placement status and expected salary based on academic and skill-based features.

---

## Overview

This project uses classification and regression models to analyze student data and generate predictions for:
- Placement status (Placed / Not Placed)
- Expected salary (for placed students)

It also includes an interactive web application for real-time predictions.

---

## Features

- Placement prediction using machine learning
- Salary prediction model
- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Interactive web interface

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  

---

## Project Structure

'''
Campus-Placement-Prediction/
│
├── data/
│   ├── placement_data.csv
│   └── salary_data.csv
│
├── models/
│   ├── placement_model.pkl
│   └── salary_model.pkl
│
├── notebooks/
│   └── preprocessing.ipynb
│
├── src/
│   ├── placement_prediction.py
│   └── salary_prediction.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
'''

---

## Dataset

The dataset contains student-related features such as:
- CGPA  
- Technical skills  
- Communication skills  
- Internships / experience  
- Other academic attributes  

**Target variables:**
- Placement status (Yes/No)  
- Salary (numerical value)

---

## Models Used

- Classification model for placement prediction  
- Regression model for salary prediction  

*(Update with actual models used, e.g., Logistic Regression, Random Forest, etc.)*

---

## How to Run

1. Clone the repository:

  git clone https://github.com/nitheesh011109/Campus-Placement-Prediction.git
<br>
  cd Campus-Placement-Prediction


2. Install dependencies:

  pip install -r requirements.txt


3. Run the application:

  streamlit run app.py


---

## Application

The project includes an interactive interface built using Streamlit, where users can input student details and receive predictions for placement and salary.

---

## Results

- Generates predictions based on trained models  
- Helps identify key factors influencing placement  
- Useful for students and training institutions  

*(Add model accuracy if available)*

---

## Future Improvements

- Improve model performance  
- Use advanced algorithms  
- Deploy the application online  
- Expand dataset  

---

## Author

Vengoti Nitheesh Reddy
GitHub: https://github.com/nitheesh011109  
LinkedIn: https://www.linkedin.com/in/nitheeshvengoti/

---

## License

This project is open-source and available under the MIT License.
