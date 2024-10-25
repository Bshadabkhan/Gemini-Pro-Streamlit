# import streamlit as st
# import google.generativeai as genai

# st.title("Generative AI content generator")

# prompt = st.text_input("Enter your response","Explain how AI works")

# generate_button = st.button("Generate content")

# response_placeholder = st.empty

# # genai.configure(api_key="AIzaSyCMhHTQ4XwWuN_aMhxBkEkE7fF6VYeL550")

# api_key = "AIzaSyCMhHTQ4XwWuN_aMhxBkEkE7fF6VYeL550"

# # model = genai.GenerativeModel("gemini-1.5-flash")

# if generate_button:
#     if prompt:
#         model = genai.GenerativeModel(api_key=api_key,model="gemini-1.5-flash")
#         response = model.generate_content(prompt)

#         response_placeholder.write (response)

# else:
#     st.warning("Please Enter a prompt")


# response = model.generate_content("Explain how AI works")

# print(response.text)


# import streamlit as st
# import google.generativeai as genai

# # Set up the API key globally (assuming this method exists)
# genai(api_key="AIzaSyBWdbA4qDD1xFaCW7thx_SIoirZRUqpxWY")

# # Streamlit UI setup
# st.title("Generative AI Content Generator")

# # Input field for the user to enter a prompt
# prompt = st.text_input("Enter your prompt", "Explain how AI works")

# # Button to trigger content generation
# generate_button = st.button("Generate Content")

# # Placeholder for the response
# response_placeholder = st.empty()

# # Only run content generation when the button is clicked
# if generate_button:
#     if prompt:
#         # Initialize the GenerativeModel with the appropriate model (no api_key needed here)
#         model = genai.annotationsGenerativeModel(model="gemini-1.5-flash")
        
#         # Generate the AI response based on the prompt
#         response = model.generate_content(prompt)
        
#         # Display the generated content
#         response_placeholder.write(response.text)
#     else:
#         st.warning("Please enter a prompt.")


# import streamlit as st
# import google.generativeai as genai

# # Streamlit UI setup
# st.title("Generative AI Content Generator")

# # Input field for the user to enter a prompt
# prompt = st.text_input("Enter your prompt", "Explain how AI works")

# # Button to trigger content generation
# generate_button = st.button("Generate Content")

# # Placeholder for the response
# response_placeholder = st.empty()

# # Configure the API key
# api_key = "AIzaSyCMhHTQ4XwWuN_aMhxBkEkE7fF6VYeL550"
# genai.configure(api_key=api_key)

# # Only run content generation when the button is clicked
# if generate_button:
#     if prompt:
#         # Generate the AI response based on the prompt
#         response = genai.generate_text(model="gemini-1.5-turbo", prompt=prompt)
        
#         # Display the generated content
#         response_placeholder.write(response.result)
#     else:
#         st.warning("Please enter a prompt.")


# import streamlit as st
# import google.generativeai as genai

# # Streamlit UI setup
# st.title("Generative AI Content Generator")

# # Input field for the user to enter a prompt
# prompt = st.text_input("Enter your prompt", "Explain how AI works")

# # Button to trigger content generation
# generate_button = st.button("Generate Content")

# # Placeholder for the response
# response_placeholder = st.empty()

# # Configure the API key
# api_key = "AIzaSyCMhHTQ4XwWuN_aMhxBkEkE7fF6VYeL550"
# genai.configure(api_key=api_key)

# # Only run content generation when the button is clicked
# if generate_button:
#     if prompt:
#         # Use the correct model name with 'models/' prefix
#         response = genai.generate_text(model="models/gemini-1.5-turbo", prompt=prompt)
        
#         # Display the generated content
#         response_placeholder.write(response.result)
#     else:
#         st.warning("Please enter a prompt.")


# import streamlit as st
# import google.generativeai as genai

# # Streamlit UI setup
# st.title("Generative AI Content Generator")

# # Input field for the user to enter a prompt
# prompt = st.text_input("Enter your prompt", "Explain how AI works")

# # Button to trigger content generation
# generate_button = st.button("Generate Content")

# # Placeholder for the response
# response_placeholder = st.empty()

# # Configure the API key
# api_key = "AIzaSyCMhHTQ4XwWuN_aMhxBkEkE7fF6VYeL550"
# genai.configure(api_key=api_key)

# # Only run content generation when the button is clicked
# if generate_button:
#     if prompt:
#         # Use the correct model name with 'models/' or 'tunedModels/' prefix
#         model_name = "models/gemini-1.5-flash-latest"  # Update this based on available models
#         try:
#             response = genai.generate_text(model=model_name, prompt=prompt)
#             # Display the generated content
#             response_placeholder.write(response.result)
#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")
#     else:
#         st.warning("Please enter a prompt.")


# import streamlit as st
# import google.generativeai as genai

# # Streamlit UI setup
# st.title("Generative AI Content Generator")

# # Input field for the user to enter a prompt
# prompt = st.text_input("Enter your prompt", "Explain how AI works")

# # Button to trigger content generation
# generate_button = st.button("Generate Content")

# # Placeholder for the response
# response_placeholder = st.empty()

# # Configure the API key
# api_key = "AIzaSyBO5kKzPLX3XU173iQFJVC-1eliBEdGojY"  # Replace with your actual API key
# genai.configure(api_key=api_key)

# # Only run content generation when the button is clicked
# if generate_button:
#     if prompt:
#         # Use the correct model name with 'models/' or 'tunedModels/' prefix
#         model_name = "models/gemini-1.5-flash-latest"  # Update this based on available models
#         try:
#             response = genai.generate_text(model=model_name, prompt=prompt)
#             # Display the generated content with a clear label
#             response_placeholder.markdown("**Generated Content:**")
#             response_placeholder.write(response.result)
#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")
#     else:
#         st.warning("Please enter a prompt.")


# import streamlit as st
# import google.generativeai as genai

# # Configure your API key
# api_key = "AIzaSyCMhHTQ4XwWuN_aMhxBkEkE7fF6VYeL550"  # Replace with your actual API key
# genai.configure(api_key=api_key)

# # Streamlit UI setup
# st.title("Gemini AI Chatbot")

# # Initialize session state to keep track of conversation
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Function to generate responses
# def get_response(user_input):
    
#     model_name = "models/gemini-1.5"  # Ensure this is the correct model name
#     response = genai.generate_text(model=model_name, prompt=user_input)
#     return response.result

# # Input field for user message
# user_input = st.text_input("You: ", "")

# # Button to send message
# if st.button("Send"):
#     if user_input:
#         # Store user input in session state
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         # Generate AI response
#         ai_response = get_response(user_input)
#         st.session_state.messages.append({"role": "ai", "content": ai_response})
        
#         # Clear the input box
#         user_input = ""

# # Display the conversation
# for message in st.session_state.messages:
#     if message['role'] == 'user':
#         st.write(f"**You:** {message['content']}")
#     else:
#         st.write(f"**AI:** {message['content']}")


import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("AIzaSyBggQl8vACqMb07oiOz9YhF9eFQeiKbf60")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key="AIzaSyBggQl8vACqMb07oiOz9YhF9eFQeiKbf60")
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

