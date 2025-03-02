from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "AIzaSyCWuCdqFk8bcpRa7xs-E9jGvij71TWH22A")

#function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response

'''#initialize our streamlit app
st.set_page_config(page_title="Question and Answer Demo") #title of the streamlit app

st.header("Tourist AI") #header of app

#input=st.text_input('Enter your question: ',key='input') #taking input from user
#submit = st.button("Ask the question") #submit button'''

'''if submit:
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)'''

inp = input("Enter question : ")
if inp:
    response = get_gemini_response(inp)
    print(response)