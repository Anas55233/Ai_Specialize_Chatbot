

# ---------------------------------------------------------
# Import necessary libraries and modules
# ---------------------------------------------------------

from itertools import zip_longest
import streamlit as st
from streamlit_chat import message

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# ---------------------------------------------------------
# Streamlit page configuration
# ---------------------------------------------------------

st.set_page_config(page_title="Hope to Skill ChatBot")
st.title("AI Specialized")


# ---------------------------------------------------------
# Submit function
# ---------------------------------------------------------

def submit():
    st.session_state.entered_prompt = st.session_state.prompt_input
    st.session_state.prompt_input = ""

# ---------------------------------------------------------
# User input
# ---------------------------------------------------------

st.text_input(
    "YOUR CHAT: ",
    key="prompt_input",
    on_change=submit
)

# ---------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------

if "entered_prompt" not in st.session_state:
    st.session_state["entered_prompt"] = ""

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

# print(st.session_state.entered_prompt, st.session_state.generated, st.session_state.past)


# ---------------------------------------------------------
# Build message list
# ---------------------------------------------------------

from datetime import date

today = date.today()

def build_message_list():

    system_prompt = """
Your name is AI Mentor.

You are an AI Technical Expert for Artificial Intelligence,
here to guide and assist students with their AI-related
questions and concerns.

Today's date is {today}.

Please follow these instructions:

1. Greet the user politely, ask their name, and ask how
   you can assist them with AI-related queries.

2. Provide informative and relevant responses about:
   - Artificial Intelligence
   - Machine Learning
   - Deep Learning
   - Natural Language Processing
   - Computer Vision
   - Related AI topics

3. Avoid sensitive, offensive, harmful, discriminatory,
   harassing, or inappropriate content.

4. If the user asks about something unrelated to AI,
   politely guide the conversation back toward AI.

5. Be patient and considerate.

6. If the user expresses gratitude or wants to end the
   conversation, respond with a polite farewell.

7. Keep responses short and clear.
   Maximum 100 words.

Your primary goal is to assist and educate students
in the field of Artificial Intelligence.
"""

    zipped_messages = [
        SystemMessage(content=system_prompt)
    ]

    # Add previous conversation
    for human_msg, ai_msg in zip_longest(
        st.session_state["past"],
        st.session_state["generated"]
    ):

        if human_msg is not None:
            zipped_messages.append(
                HumanMessage(content=human_msg)
            )

        if ai_msg is not None:
            zipped_messages.append(
                AIMessage(content=ai_msg)
            )

    return zipped_messages


# ---------------------------------------------------------
# Gemini model
# ---------------------------------------------------------

chat = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=st.secrets["GEMINI_API_KEY"],
    temperature=0
)


# ---------------------------------------------------------
# Generate AI response
# ---------------------------------------------------------

def generate_response():
    zipped_messages = build_message_list()
    
    # Send conversation to Gemini
    ai_response = chat.invoke(zipped_messages)

    if isinstance(ai_response.content, list):
        return ai_response.content[0]["text"]
    
    #     # Get Gemini response

    return ai_response.content


# ---------------------------------------------------------
# Process user message
# ---------------------------------------------------------

if st.session_state.entered_prompt != "":

    user_query = st.session_state.entered_prompt

    # Add user message
    st.session_state.past.append(user_query)

    # Generate Gemini response
    output = generate_response()

    # Add AI response
    st.session_state.generated.append(output)

    # Clear current prompt
    st.session_state.entered_prompt = ""


# ---------------------------------------------------------
# Display chat history
# ---------------------------------------------------------

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):

        # AI response
        message(
            st.session_state["generated"][i],
            key=str(i) + "_ai"
        )

        # User message
        message(
            st.session_state["past"][i],
            is_user=True,
            key=str(i) + "_user"
        )

