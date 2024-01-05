import streamlit as st


gemini_api_key = os.getenv("GEMINI_API_KEY")


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)

to_markdown(response.text)

import google.generativeai as genai

genai.configure(api_key = gemini_api_key)

# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("What is the meaning of life?")

# Define a function that will be called when the user clicks the button
def greet_user():
    # Get the user's name from the text input
    name = st.text_input("Enter your name:")

    # Greet the user
    st.write(f"Hello, {name}!")

# Add a button to the app
st.button("Greet me!", greet_user)



st.title("Hello! Streamlit App")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)



# st.title('AI Fitness Trainer: Squats Analysis')


# recorded_file = 'output_sample.mp4'
# sample_vid = st.empty()
# sample_vid.video(recorded_file)
