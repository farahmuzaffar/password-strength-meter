import re
import random
import string
import streamlit as st # type: ignore



def check_password_strength(password):
    score = 0
    feedback = []


    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

  
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

  
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback


def generate_strong_password(length=8):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))


st.title("🔐 Password Strength Meter")


password = st.text_input("Enter your password", type="password", key="password_input")



if password:
    score, feedback = check_password_strength(password)
    
    
    st.markdown("💪 Password Strength")
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_color = ["red", "orange", "yellow", "lightgreen", "green"]
    strength_index = min(score, 4) 
    st.progress((score + 1) / 5)  
    st.markdown(f"**Strength Level:** :{strength_color[strength_index]}[{strength_levels[strength_index]}]")

    
    if score <= 2:
        st.error("❌ Weak Password - Improve it using the suggestions below:")
    elif score <= 4:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.success("✅ Strong Password! Your password meets all the criteria.")

   
    if feedback:
        st.markdown("Feedback:")
        for item in feedback:
            st.markdown(item)


st.markdown("---")
st.markdown("💪 Generate a Strong Password")


password_length = st.slider("Select password length", min_value=8, max_value=20, value=12)


if st.button("🔏Generate Strong Password"):
    suggested_password = generate_strong_password(password_length)
    st.success(f"**Suggested Password:** `{suggested_password}`")

  
    if st.button("Copy to Clipboard"):
        st.write("📋 Password copied to clipboard!")
        st.experimental_set_query_params(password=suggested_password)  





