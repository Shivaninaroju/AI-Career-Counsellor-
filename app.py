# app.py
import streamlit as st
from typing import List
import sys
import os

# Add the path to RASA backend/actions to Python path
sys.path.append(os.path.join(os.getcwd(), "rasa_backend", "actions"))

from actions import ActionSmartChat  # now Python can find it
  # import your smart action

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages: List[dict] = []

st.title("💬 AI Career Counsellor")

# User input
user_input = st.text_input("Type your message here:")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call the smart chat action
    action = ActionSmartChat()
    class TrackerMock:
        def __init__(self, text):
            self.latest_message = {"text": text}
    tracker = TrackerMock(user_input)

    class DispatcherMock:
        def __init__(self):
            self.messages = []

        def utter_message(self, text):
            self.messages.append(text)

    dispatcher = DispatcherMock()
    action.run(dispatcher, tracker, domain={})

    # Add bot responses to chat history
    for msg in dispatcher.messages:
        st.session_state.messages.append({"role": "bot", "content": msg})

# Display chat messages
for chat in st.session_state.messages:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Bot:** {chat['content']}")
