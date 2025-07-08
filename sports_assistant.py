import streamlit as st
import os
from groq import Groq
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Sports Assistant",
    page_icon="🏆",
    layout="centered"
)

# Initialize Groq client
def initialize_groq():
    api_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
    if not api_key:
        st.error("GROQ API key not found. Please set it in your Streamlit secrets or as an environment variable.")
        st.stop()
    return Groq(api_key=api_key)

# App title and description
st.title("🏆 Sports Assistant")
st.markdown("Get answers about your favorite sports, teams, players, and events!")

# Sidebar with sport selection
st.sidebar.header("Select a Sport")
selected_sport = st.sidebar.selectbox(
    "Choose a sport to focus on",
    ["All Sports", "Football/Soccer", "Basketball", "Cricket", "Tennis", "Baseball", 
     "American Football", "Golf", "Formula 1", "Boxing", "MMA"]
)

# Display selected sport in the main area
st.markdown(f"### Currently focused on: **{selected_sport}**")
st.markdown("---")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate response from Groq
def get_groq_response(prompt, sport):
    client = initialize_groq()
    
    # Current date information for context
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Create system prompt based on sport selection
    system_prompt = f"""You are a helpful sports assistant specializing in {sport if sport != 'All Sports' else 'all sports'}. 
    Today is {current_date}. 
    Provide accurate, concise answers to sports-related queries.
    Include relevant statistics, recent events, team information, and player details when appropriate.
    If you don't know the answer or if the information might be outdated (particularly for very recent events), acknowledge this limitation.
    Focus on being helpful rather than exhaustive - prioritize the most relevant information.
    Keep responses conversational and engaging."""
    
    try:
        # Get completion from Groq
        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Using Llama 3 70B model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error communicating with Groq: {str(e)}"

# User input
if prompt := st.chat_input("Ask about sports, teams, players, or events..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with a loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Generate response considering the selected sport
            sports_context = f"Answer the following question about {selected_sport}: {prompt}" if selected_sport != "All Sports" else prompt
            response = get_groq_response(sports_context, selected_sport)
            
            # Show response
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Instructions in sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. Select a sport from the dropdown menu")
    st.markdown("2. Ask any sports-related question")
    st.markdown("3. Get AI-powered answers about teams, players, scores, and more")
    
    st.markdown("---")
    st.markdown("### Example Questions:")
    st.markdown("- Who won the last World Cup?")
    st.markdown("- What are the NBA standings?")
    st.markdown("- When is the next Grand Slam tennis tournament?")
    st.markdown("- Tell me about Cristiano Ronaldo's career")
    st.markdown("- What were the highlights from yesterday's games?")

# Add option to clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# Setup instructions (hidden in an expander)
with st.sidebar.expander("Setup Instructions"):
    st.markdown("""
    ### Setup Instructions:
    
    1. **Groq API Key**: You need to set up your Groq API key:
       - Create a `.streamlit/secrets.toml` file with:
         ```
         GROQ_API_KEY = "your_groq_api_key"
         ```
       - Or set it as an environment variable before running the app
    
    2. **Installation**: Install the required packages:
       ```
       pip install streamlit groq
       ```
    
    3. **Running the app**:
       ```
       streamlit run app.py
       ```
    """)




    # syntax to run the code :  streamlit run sports_assistant.py   