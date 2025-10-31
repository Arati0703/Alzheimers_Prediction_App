import streamlit as st
import numpy as np

st.set_page_config(page_title="Alzheimer’s Risk Predictor", page_icon="🧠")

st.title("🧠 Alzheimer’s Disease Risk Prediction Web App")
st.write("This app helps you understand potential risk factors based on lifestyle, memory score, and personal habits.")
st.divider()

# --- SECTION 1: Memory Game Score ---
st.subheader("🎮 Memory Game Score")
memory_score = st.selectbox("Select your Memory Game Score (0–6):", list(range(7)))

st.divider()

# --- SECTION 2: User Inputs (Dropdowns) ---
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

# --- SECTION 3: Predict Button ---
if st.button("🔍 Predict Alzheimer’s Risk"):
    # Basic dummy risk scoring logic
    score = 0

    if age_group in ["60-70", "Above 70"]:
        score += 2
    if sleep in ["Less than 5 hrs", "More than 9 hrs"]:
        score += 1
    if activity == "Low":
        score += 2
    if diet == "Poor":
        score += 2
    if stress == "High":
        score += 1
    if family_history == "Yes":
        score += 2
    if mood == "Sad":
        score += 1
    if education in ["Primary", "Secondary"]:
        score += 1

    # Include memory score
    score += (6 - memory_score)

    # --- Display Results ---
    st.divider()
    st.subheader("🎯 Prediction Result")

    if score <= 3:
        st.success("✅ Low Risk of Alzheimer’s Disease")
        st.write("""
        Your responses show strong memory and healthy lifestyle habits.  
        🧠 You’re doing great — keep your mind active through reading, games, and conversations.  
        🌼 *Every healthy habit you build strengthens your brain for the future!*
        """)
    elif 4 <= score <= 6:
        st.warning("⚠️ Moderate Risk Detected")
        st.write("""
        Some habits may slightly affect memory and focus.  
        🌿 Don’t worry — regular sleep, a balanced diet, and brain exercises can sharpen your mind.  
        💪 *You’ve already taken the first step by checking your brain health today!*
        """)
    else:
        st.error("🚨 High Risk of Alzheimer’s Disease")
        st.write("""
        Your answers show several signs that may increase the risk.  
        💙 You are not alone — many people improve with early lifestyle changes and guidance.  
        🩺 Please consult a healthcare expert for more advice.  
        🌻 *Courage is the first step toward healing — and you’ve already taken it.*
        """)

    # Show recap
    st.divider()
    st.write(f"🧠 **Your Memory Score:** {memory_score} / 6")
    st.write(f"📋 **Total Risk Points:** {score}")

