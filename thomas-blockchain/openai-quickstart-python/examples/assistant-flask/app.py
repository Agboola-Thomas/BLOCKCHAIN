import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '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'

# Streamlit App
st.title("Movie Character Name Generator")

# Input prompt from the user
prompt = st.text_input("Enter a prompt to generate movie character names:")

# Function to generate movie character names using OpenAI
def generate_character_names(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or use another engine of your choice
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ""

# Generate character names when the user submits a prompt
if st.button("Generate Names"):
    if prompt:
        names = generate_character_names(prompt)
        st.subheader("Generated Movie Character Names:")
        st.write(names)
    else:
        st.warning("Please enter a prompt to generate names.")
