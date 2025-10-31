import streamlit as st
import numpy as np

# --- Page setup ---
st.set_page_config(page_title="Alzheimer’s Risk Predictor", page_icon="🧠")

st.title("🧠 Alzheimer’s Disease Risk Prediction Web App")
st.write("""
Welcome!  
This app helps you check your **memory strength** through a short quiz  
and then predicts your **Alzheimer’s risk level** based on lifestyle habits.  
""")

st.divider()

# ----------------------------
# PART 1: MEMORY QUIZ
# ----------------------------
st.subheader("🎮 Memory Check Game (6 Questions)")
st.write("Answer these 6 quick questions to test your short-term memory!")

score = 0  # memory score counter

# Q1
st.write("**1️⃣ What was the color of the 'Start' button you clicked?**")
q1 = st.radio("Choose your answer:", ["Red", "Green", "Blue", "Yellow"], key="q1")
if q1 == "Green":
    score += 1

# Q2
st.write("**2️⃣ Which day comes after Wednesday?**")
q2 = st.radio("Choose your answer:", ["Monday", "Thursday", "Friday", "Tuesday"], key="q2")
if q2 == "Thursday":
    score += 1

# Q3
st.write("**3️⃣ How many sides does a hexagon have?**")
q3 = st.radio("Choose your answer:", ["5", "6", "8", "4"], key="q3")
if q3 == "6":
    score += 1

# Q4
st.write("**4️⃣ What animal is known as the ‘King of the Jungle’?**")
q4 = st.radio("Choose your answer:", ["Tiger", "Elephant", "Lion", "Leopard"], key="q4")
if q4 == "Lion":
    score += 1

# Q5
st.write("**5️⃣ Remember this number: 4279**")
st.info("Now scroll down and answer the next question 👇")

# Q6
st.write("**6️⃣ What was the number shown just above?**")
q6 = st.text_input("Enter the number:")
if q6.strip() == "4279":
    score += 1

# Show memory score
if st.button("✅ Submit Memory Quiz"):
    st.success(f"🧠 Your Memory Score: {score} / 6")
    st.session_state["memory_score"] = score  # store score for later

st.divider()

# ----------------------------
# PART 2: LIFESTYLE INPUTS
# ----------------------------
st.subheader("🩺 Lifestyle and Health Details")

age_group = st.selectbox("Select Age Group:", ["Below 50", "50-60", "60-70", "Above 70"])
sleep = st.selectbox("Sleep Duration per Day:", ["Less than 5 hrs", "5-7 hrs", "7-9 hrs", "More than 9 hrs"])
activity = st.selectbox("Physical Activity Level:", ["Low", "Moderate", "High"])
diet = st.selectbox("Diet Quality:", ["Poor", "Average", "Good"])
stress = st.selectbox("Stress Level:", ["Low", "Moderate", "High"])
family_history = st.selectbox("Family History of Alzheimer’s:", ["No", "Yes"])
mood = st.selectbox("Overall Mood:", ["Happy", "Neutral", "Sad"])
education = st.selectbox("Education Level:", ["Primary", "Secondary", "Graduate", "Post-Graduate"])

st.divider()

# ----------------------------
# PART 3: RISK PREDICTION
# ----------------------------
if st.button("🔍 Predict Alzheimer’s Risk"):
    memory_score = st.session_state.get("memory_score", 0)
    total_score = 0

    # Basic scoring rules
    if age_group in ["60-70", "Above 70"]:
        total_score += 2
    if sleep in ["Less than 5 hrs", "More than 9 hrs"]:
        total_score += 1
    if activity == "Low":
        total_score += 2
    if diet == "Poor":
        total_score += 2
    if stress == "High":
        total_score += 1
    if family_history == "Yes":
        total_score += 2
    if mood == "Sad":
        total_score += 1
    if education in ["Primary", "Secondary"]:
        total_score += 1

    # Lower memory score increases risk
    total_score += (6 - memory_score)

    st.divider()
    st.subheader("🎯 Prediction Result")

    # Show results + positivity
    if total_score <= 3:
        st.success("✅ Low Risk of Alzheimer’s Disease")
        st.write("""
        Your memory score and lifestyle look great!  
        🧠 Keep your brain active through puzzles, reading, and social interaction.  
        🌼 *Healthy habits today protect your mind for tomorrow.*
        """)
    elif 4 <= total_score <= 6:
        st.warning("⚠️ Moderate Risk Detected")
        st.write("""
        You show some signs that can slightly affect memory and focus.  
        🌿 Try improving your sleep and staying physically active.  
        💪 *You’ve already taken a great step by being proactive today!*
        """)
    else:
        st.error("🚨 High Risk of Alzheimer’s Disease")
        st.write("""
        Your answers show multiple possible risk factors.  
        💙 Don’t worry — early awareness helps prevention!  
        🩺 Please consult a healthcare expert for proper evaluation.  
        🌻 *Every effort counts toward a healthier mind.*
        """)

    st.divider()
    st.write(f"🧠 **Your Memory Score:** {memory_score} / 6")
    st.write(f"📋 **Total Risk Points:** {total_score}")
    st.progress(min(total_score, 10) / 10)

