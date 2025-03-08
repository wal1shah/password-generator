import re
import streamlit as st
import pyperclip  # For copying text to clipboard

# Configure the page layout and title
st.set_page_config(page_title="Password Strength Checker", layout="centered")

# Initialize session state for password
if "password" not in st.session_state:
    st.session_state.password = ""

# Add vertical spacing in the main app
st.write("")

# App title and description
st.title("Password Strength Checker")
st.write("Check your password strength and get tips to improve it!")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check if password is at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔒 Password should be at least **8 characters long**.")

    # Check if password contains both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔠 Password should include **both uppercase and lowercase letters**.")

    # Check if password contains at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Password should include **at least one number (0-9)**.")

    # Check if password contains at least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("✨ Password should include **at least one special character (!@#$%^&*)**.")

    # Calculate strength percentage
    strength_percentage = (score / 4) * 100

    # Display password strength result
    if score == 4:
        st.success("🎉 **Strong Password!** ✅✅")
    elif score == 3:
        st.info("🛠️ **Medium Password** - Consider adding more complexity 🔏")
    else:
        st.error("⚠️ **Weak Password** - Checkout suggestions to improve it 👇")

    # Show password strength meter
    st.markdown(f"""
    <div class="progress-bar">
        <div class="progress-bar-fill" style="width: {strength_percentage}%;"></div>
    </div>
    <p>Strength: {strength_percentage}%</p>
    """, unsafe_allow_html=True)

    # Show feedback for improving the password
    if feedback:
        st.markdown("<div class='suggestions'><h4>💡 Tips to Improve Your Password:</h4>", unsafe_allow_html=True)
        for tip in feedback:
            st.markdown(f"- {tip}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Input field for the password
password = st.text_input(
    "Enter your password:",
    value=st.session_state.password,  # Use session state for the input value
    type="password",
    help="Ensure your password meets the criteria above."
)

# Update session state with the new password value
st.session_state.password = password

# Button to check password strength
if st.button("Check Password Strength"):
    if st.session_state.password:
        check_password_strength(st.session_state.password)
    else:
        st.warning("Please enter a password first!")

# Password requirements checklist
st.markdown("<div class='suggestions'><h4>🔑 Password Requirements:</h4>", unsafe_allow_html=True)
st.write("")
st.markdown("""
- At least 8 characters long
- Includes both uppercase and lowercase letters
- Includes at least one number (0-9)
- Includes at least one special character (!@#$%^&*)
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Educational tips section
st.markdown("<div class='suggestions'><h4>📚 Password Best Practices:</h4>", unsafe_allow_html=True)
st.write("")
st.markdown("""
- Use a unique password for each account.
- Avoid using common words or phrases.
- Consider using a password manager to store your passwords securely.
- Change your passwords regularly.
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Reset button to clear the input
if st.button("Reset"):
    st.session_state.password = "" 
    st.rerun()  