import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="From My Heart to Yours",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Montserrat:wght@300;400;500&display=swap');
    
    .main {
        background-color: #faf7f5;
        color: #555555;
    }
    
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif;
        color: #9b6a6c;
    }
    
    p {
        font-family: 'Montserrat', sans-serif;
        line-height: 1.7;
        font-weight: 300;
    }
    
    .stButton>button {
        background-color: #d4b8b3;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        font-family: 'Montserrat', sans-serif;
        font-weight: 400;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #9b6a6c;
        transform: scale(1.05);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    .message-container {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin: 20px 0;
    }
    
    .highlight {
        color: #9b6a6c;
        font-weight: 500;
    }
    
    .divider {
        height: 2px;
        background-color: #f0e6e6;
        margin: 20px 0;
    }
    
    .date {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        color: #aaa;
        text-align: right;
    }
    
    .centered-text {
        text-align: center;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation - healing heart
lottie_heart = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_btTdcr.json")

# Display header with subtle animation
st.markdown("<h1 class='centered-text'>From My Heart to Yours</h1>", unsafe_allow_html=True)

# Display date
today = datetime.now().strftime("%B %d, %Y")
st.markdown(f"<p class='date'>{today}</p>", unsafe_allow_html=True)

# Main content container
st.markdown("<div class='message-container'>", unsafe_allow_html=True)

# Greeting
st.markdown("<p>Dear <span class='highlight'>Love</span>,</p>", unsafe_allow_html=True)

# Main apology text
st.markdown("""
<p>I'm writing to you with a heavy heart and sincere regret for the pain I've caused. Words cannot fully express how deeply sorry I am for hurting you. My actions were thoughtless, and I take full responsibility for the hurt they've caused. You deserved so much better than what I gave you.</p>

<p>What we had was special, and I failed to honor that. I've spent every day since reflecting on my mistakes and wishing I could turn back time. Not to erase what happened, but to make different choices—choices that would have protected your heart rather than wounded it.</p>

<div class='divider'></div>

<p style='font-family: "Cormorant Garamond", serif; font-size: 20px; font-style: italic; text-align: center; color: #9b6a6c;'>
Like petals fallen from a cherished rose,<br>
I gather moments we've lost to the wind.<br>
In the silence between us, my regret grows,<br>
Longing for the chance to begin again.<br>
My heart reaches across the distance I created,<br>
Hoping yours might still hear its sincere beat.<br>
</p>

<div class='divider'></div>

<p>I understand that forgiveness isn't something I'm entitled to, but something I need to earn. I'm committed to growing from this experience and becoming someone worthy of your trust again—even if that's as a distant memory rather than a present reality.</p>

<p>I miss your smile, your laughter, the way you see the world. Most of all, I miss being someone who brought joy to your life rather than pain.</p>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Animation
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st_lottie(lottie_heart, height=200)

# Question and response buttons
st.markdown("<div class='message-container'>", unsafe_allow_html=True)
st.markdown("<p class='centered-text'>Can you find it in your heart to forgive me?</p>", unsafe_allow_html=True)

# Button container
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("I Forgive You"):
        st.markdown("""
        <div style='background-color: #f0f9f0; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3>Thank You ❤️</h3>
            <p>Your forgiveness means everything to me. I promise to honor your trust and be better moving forward.</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("I Need Time"):
        st.markdown("""
        <div style='background-color: #f9f7f0; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3>I Understand 🕊️</h3>
            <p>Take all the time you need. Healing happens at its own pace, and I'll respect your journey.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer with quote
st.markdown("""
<div style='margin-top: 40px; text-align: center; font-family: "Cormorant Garamond", serif; font-style: italic; color: #aaa;'>
"The first to apologize is the bravest.<br>
The first to forgive is the strongest.<br>
The first to forget is the happiest."
</div>
""", unsafe_allow_html=True)

# Add message input for response
st.markdown("<div class='message-container' style='margin-top: 30px;'>", unsafe_allow_html=True)
st.markdown("<p class='centered-text'>If you'd like to share your thoughts:</p>", unsafe_allow_html=True)
user_message = st.text_area("", placeholder="Write your message here...", height=100)

if st.button("Send Your Message"):
    if user_message:
        st.success("Thank you for sharing your feelings. I appreciate your honesty and will treasure your words.")
    else:
        st.warning("Please write a message before sending.")
        
st.markdown("</div>", unsafe_allow_html=True)