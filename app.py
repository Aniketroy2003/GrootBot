import streamlit as st
import google.generativeai as genai


# Function to call OpenAI API and get response
def generate_response(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    return response.text

def main():
    st.title("Groot (The chat bot)")
    st.markdown("How may I help you?")

    api_key = "AIzaSyDVwznMhukxzTq9PAv67y-dD8TGnHKLa3M"
    
    # Input field for user's message
    user_input = st.text_input("You:", key="user_input")
    
    if st.button("Send"):
        # Generate response
        response = generate_response(user_input, api_key)
        # Display user's message
        st.text_area("You:", value=user_input, disabled=True)
        # Display model's response
        st.text_area("AI:", value=response, disabled=True, height=300)

if __name__ == "__main__":
    main()
