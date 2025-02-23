import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initialize the chatbot pipeline
chatbot = pipeline("text-generation", model="distilgpt2")

# Define the healthcare chatbot function
def healthcare_chatbot(user_input):
    """
    Generate a response to the user's input.
    """
    if "symptom" in user_input.lower():
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input.lower():
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input.lower():
        return "It's essential to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']


def main():

    st.title("Healthcare Assistant Chatbot")

    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a message to get a response.")

if __name__ == "__main__":
    main()