# Student Performance Prediction System
**Live Demo:** https://student-performance-prediction-kavya.streamlit.app

**GitHub:** https://github.com/skavyasri156-coder/student-performance-prediction

A machine learning web application that predicts whether a student's
performance is **Good**, **Average** or **Poor**, built with Python,
scikit-learn and Streamlit.

## Features
- Enter attendance, study hours, previous marks and assignment score
- Get an instant performance prediction
- See model confidence as a table and bar chart

## Tech Stack
- Python
- Pandas, NumPy
- scikit-learn (Decision Tree Classifier)
- Streamlit
- Joblib
- Matplotlib

## Project Structure
- `app.py` : Streamlit web application
- `make_dataset.py` : creates the synthetic dataset
- `train_final_model.py` : trains and saves the final model
- `compare_models.py` : compares models using cross-validation
- `dataset/students_big.csv` : dataset (60 records)
- `student_model_final.pkl` : saved trained model

## How to Run
1. Install the libraries:
   pip install -r requirements.txt
2. Start the app:
   python -m streamlit run app.py

## Model Results
- Algorithm: Decision Tree Classifier (max_depth = 5)
- Cross-validation accuracy: about 71.67% (5-fold)
- Random Forest was also tested (about 68.33%)

## Important Note
The dataset is **synthetic** (computer-generated) and has only 60 records.
This project is a learning prototype. Accuracy can improve with larger,
real student data.

## Author
S. Kavyasri, B.Tech CSE (Data Science)