import streamlit as st
import google.generativeai as genai
import os


gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel('gemini-pro')



# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
# else:
#     prompt = "who are you?"
# response = model.generate_content(prompt)
# message = st.chat_message("ai")
# message.write(response.text)


import string
import random


def randon_string() -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


def chat_actions():
    st.session_state["chat_history"].append(
        {"role": "user", "content": st.session_state["chat_input"]},
    )

    response = model.generate_content(st.session_state["chat_input"])
    st.session_state["chat_history"].append(
        {
            "role": "assistant",
            "content": response,
        },  # This can be replaced with your chat response logic
    )


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


st.chat_input("Enter your message", on_submit=chat_actions, key="chat_input")

for i in st.session_state["chat_history"]:
    with st.chat_message(name=i["role"]):
        st.write(i["content"])