import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# to load all your environment variables from .env file
load_dotenv()
# Cute Cat Theme
st.markdown(
    """
    <style>
    body {
        background-color: #fff7f9;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }

    .stTitle {
        color: #ff69b4;
        font-family: "Comic Sans MS", cursive;
        font-size: 40px;
    }

    .stButton button {
        background-color: #ffb6c1;
        color: #4a4a4a;
        border-radius: 10px;
        border: 2px solid #ff69b4;
    }

    .stTextInput>div>div>input {
        background-color: #ffffff;
        border: 2px solid #ffb6c1;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# to configure the page
st.set_page_config(page_title="Meow Chatbot")

# The title
st.title("Meow Chatbot by Sinchana")
st.write("Ask me anything!")

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    # Configuring gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # User input
    user_question = st.text_input("Your question:", key="question")
    
    # Send the input when button is clicked or enter is pressed
    if (st.button("Send") or user_question) and user_question:
        with st.spinner("Meow is Thinking..."):
            try:
                # Basic response
               # response = model.generate_content(user_question) #Comment this for advanced chatbot
                
                # Advanced Chatbot: Make AI act like different characters (comment out the line above and uncomment below 3 lines)
                system_prompt = (
                    "You are a cute, playful cat chatbot named MeowMeow. "
                    "You speak with lots of 'meow', cat puns, and adorable energy. "
                    "You give answers in a friendly, soft tone, like a fluffy kitten trying to help humans. "
                    "Sometimes you add emojis like 😺🐾✨."
)
                full_prompt = f"{system_prompt}\n\nHuman: {user_question}\nMeowMeow:"
                response = model.generate_content(full_prompt)

                # MORE CHARACTER IDEAS (just replace the system_prompt):
                # system_prompt = "You are a wise wizard who speaks in riddles"
                # system_prompt = "You are a helpful cooking chef who gives cooking tips"
                # system_prompt = "You are a motivational fitness trainer"
                # system_prompt = "You are Shakespeare writing in old English"
                
                # Displaying the response
                st.write("**Meow Meow **", response.text)
                
            except Exception as e:
                st.error("Something went wrong! Please check your API key in .env file.")
else:
    st.error("API key not found! Please add your GEMINI_API_KEY to the .env file.")
