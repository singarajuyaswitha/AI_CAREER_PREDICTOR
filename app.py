import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ----------------- Sidebar -----------------
st.sidebar.title("🧠 AI Career Predictor")
st.sidebar.write("Predict your best career path based on your skills.")
st.sidebar.write("Select your skills and click 'Predict Career' 🚀")

# ----------------- Main Title -----------------
st.title("🧠 AI Career Path Predictor")
st.write("Find your suitable career based on your skills 🚀")

# ----------------- Load Dataset & Train Model -----------------
data = pd.read_csv("career_data.csv")
X = data.drop("Recommended_Career", axis=1)
y = data["Recommended_Career"]
model = DecisionTreeClassifier()
model.fit(X, y)

# ----------------- Skill Selection -----------------
st.subheader("Select Your Skills 👇")

python_skill = st.selectbox("Do you know Python?", ["No", "Yes"])
ml_skill = st.selectbox("Do you know Machine Learning?", ["No", "Yes"])
web_skill = st.selectbox("Do you know Web Development?", ["No", "Yes"])
comm_skill = st.selectbox("Do you have good Communication skills?", ["No", "Yes"])
math_skill = st.selectbox("Are you good at Math?", ["No", "Yes"])

# Convert Yes/No to 1/0
python_skill = 1 if python_skill == "Yes" else 0
ml_skill = 1 if ml_skill == "Yes" else 0
web_skill = 1 if web_skill == "Yes" else 0
comm_skill = 1 if comm_skill == "Yes" else 0
math_skill = 1 if math_skill == "Yes" else 0

# ----------------- Prediction Button -----------------
if st.button("Predict Career"):
    input_data = [[python_skill, ml_skill, web_skill, comm_skill, math_skill]]
    prediction = model.predict(input_data)
    predicted_career = prediction[0]
    
    st.success(f"🎯 Recommended Career: {predicted_career}")

    # ----------------- Career Description -----------------
    st.subheader("💡 Career Description:")
    if predicted_career == "Data_Scientist":
        st.write("📊 You enjoy analyzing data, building models, and solving real-world problems with AI.")
    elif predicted_career == "Web_Developer":
        st.write("💻 You love building websites, applications, and creating interactive user experiences.")
    elif predicted_career == "Frontend_Developer":
        st.write("🎨 You enjoy designing user interfaces and working on the client-side of web applications.")

    # ----------------- Skill Gap Analysis -----------------
    st.subheader("⚠ Skill Gap Analysis:")
    if predicted_career == "Data_Scientist":
        if python_skill == 0:
            st.write("- Improve Python")
        if ml_skill == 0:
            st.write("- Learn Machine Learning")
        if math_skill == 0:
            st.write("- Improve Mathematics")
    elif predicted_career == "Web_Developer":
        if web_skill == 0:
            st.write("- Improve Web Development")
        if python_skill == 0:
            st.write("- Learn Python")
    elif predicted_career == "Frontend_Developer":
        if web_skill == 0:
            st.write("- Improve Frontend Skills (HTML, CSS, JS)")