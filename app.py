import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Date Invitation", page_icon="☕", layout="wide")

# List of quotes
quotes = [
    "You mocha me smile ☕",
    "Life happens, coffee helps ☕",
    "Espresso yourself!",
    "But first, coffee ☕",
    "Love is in the air, and it smells like coffee ☕"
]

# CSS for custom styling and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Poppins:wght@300&display=swap'); /* Import Google Fonts */
    
    body {
        background: linear-gradient(to bottom, #ffcccb, #ffefba); /* Soft pink gradient */
        color: #fff;
        font-family: 'Poppins', sans-serif; /* Changed to Poppins for better readability */
        text-align: center;
        overflow: hidden; /* Prevent scrollbars */
        position: relative;
    }
    .hero {
        padding: 50px;
        animation: glow 1.5s infinite alternate;
        font-family: 'Dancing Script', cursive; /* Playful font for headings */
    }
    @keyframes glow {
        0% { text-shadow: 0 0 10px #fff, 0 0 20px #ff69b4; }
        100% { text-shadow: 0 0 20px #fff, 0 0 30px #ff69b4; }
    }
    .message {
        font-size: 24px;
        margin: 20px;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .button {
        display: inline-block;
        margin: 10px;
        padding: 15px 30px;
        font-size: 20px;
        background-color: #ff69b4; /* Pink color */
        color: #fff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .button:hover {
        background-color: #ff1493; /* Darker pink */
        transform: scale(1.05) rotate(5deg); /* Slight bounce and rotation */
    }
    .footer {
        margin-top: 50px;
        font-size: 18px;
    }
    .hidden-message {
        display: none;
        font-size: 24px;
        margin-top: 20px;
        color: #ffcc00;
    }
    /* Coffee steam animation */
    .steam {
        position: relative;
        animation: steam 2s infinite;
    }
    @keyframes steam {
        0% { transform: translateY(0); opacity: 0.5; }
        100% { transform: translateY(-50px); opacity: 0; }
    }
    /* Checklist styles */
    .checklist {
        text-align: left;
        margin: 20px auto;
        width: 300px;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section with Coffee Steam Animation
st.markdown("<div class='hero'><h1>Hey Insaan 🌟</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='steam'>☕☕☕</div>", unsafe_allow_html=True)  # Coffee steam animation

# Quote of the Day
quote_of_the_day = random.choice(quotes)
st.markdown(f"<h2 style='color: #ff69b4;'>{quote_of_the_day}</h2>", unsafe_allow_html=True)

# Message Section
st.markdown("<div class='message'>Been craving something warm and special…<br><span id='animated-text'>Good coffee and even better company (that’s you, of course!)!</span></div>", unsafe_allow_html=True)

# Interactive Buttons
if st.button("Let’s Meet 💌", key="meet_button"):
    st.balloons()  # Show balloons
    st.markdown("<h2 style='color: #ff69b4;'>❤️❤️❤️</h2>", unsafe_allow_html=True)  # Show hearts
    st.success("🌟 Place: Coffea, NIBM\n🕕 Time: 6 PM today!\n💖 See you there!")
    st.markdown("<div style='font-size: 24px;'>Yay! Date night confirmed! ☕❤️</div>", unsafe_allow_html=True)
elif st.button("Who says no to cozy corners and me?!", key="reject_button"):
    st.error("That’s okay… but are you sure you want to miss out on me and coffee? Click above to change your mind!")

# Date Night Checklist with Icons
st.markdown("<div class='checklist'><h3>What to bring to our date:</h3><ul><li>😊 Your charming smile.</li><li>☕ Good vibes.</li><li>❤️ Lots of love for cozy conversations!</li></ul></div>", unsafe_allow_html=True)

# Footer Section
st.markdown("<div class='footer'><h3>PS: I picked Coffea because they have the best cozy corners for us to spend some quality time together. Can’t wait to see you!</h3></div>", unsafe_allow_html=True)
