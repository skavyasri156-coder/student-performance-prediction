import streamlit as st
import pandas as pd
import joblib

# 1. Page settings
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

# 2. Load the saved model (only once, to keep the app fast)
@st.cache_resource
def load_model():
    return joblib.load("student_model_final.pkl")

model = load_model()

# 3. Title and short description
st.title("🎓 Student Performance Prediction System")
st.write("Enter the student details below and click **Predict**.")

# 4. Input fields
attendance = st.slider("Attendance (%)", min_value=0, max_value=100, value=75)
study_hours = st.slider("Study hours per day", min_value=0, max_value=12, value=4)
previous_marks = st.number_input(
    "Previous marks (0 to 100)", min_value=0, max_value=100, value=60
)
assignment_score = st.number_input(
    "Assignment score (0 to 100)", min_value=0, max_value=100, value=60
)

# 5. Predict button
if st.button("Predict"):
    # Put the inputs in a table with the SAME column names used in training
    student = pd.DataFrame(
        [[attendance, study_hours, previous_marks, assignment_score]],
        columns=["attendance", "study_hours", "previous_marks", "assignment_score"],
    )

    result = model.predict(student)[0]

    # 6. Show the result with colours
    if result == "Good":
        st.success("Predicted performance: Good ✅")
    elif result == "Average":
        st.warning("Predicted performance: Average ⚠️")
    else:
        st.error("Predicted performance: Poor ❌")

    # 7. Show how confident the model is
    probabilities = model.predict_proba(student)[0]
    chances = pd.DataFrame({
        "Performance": model.classes_,
        "Chance (%)": (probabilities * 100).round(1),
    })
    st.write("Model confidence:")
    st.dataframe(chances, hide_index=True)
    st.bar_chart(chances.set_index("Performance"))

st.caption("Note: This model is trained on a small synthetic dataset. It is a learning prototype.")