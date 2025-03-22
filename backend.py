from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyCWuCdqFk8bcpRa7xs-E9jGvij71TWH22A")

# function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response

inp = input("Enter question: ")
if inp:
    # Modify the prompt to request JSON output
    prompt = f"{inp} Provide the destination, budget, and number of days in JSON format: {{'destination': '...', 'budget': '...', 'days': '...'}}."
    response = get_gemini_response(prompt)

data = json.loads(response.text)
dest = data["destination"]
budget = data["budget"]
days = data["days"]
print(f"Destination: {dest}")
print(f"Budget: {budget}")
print(f"Days: {days}")
