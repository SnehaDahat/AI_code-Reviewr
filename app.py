from openai import OpenAI 
import streamlit as sl
from dotenv import load_dotenv
import os



#load_dotenv()
#api_key = os.getenv("OPENAI_API _KEY")
client=OpenAI(api_key="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")         


sl.title("🤗 I'm an AI Code Reviewer, try your code here 😁")
prompt = sl.text_area("ENTER UR CODE BELOW:", height=200, placeholder="REVIEWER")

if sl.button("Generate") == True:
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're an AI assistant tasked with analyzing Python code submissions. Your goal is to detect any potential bugs, errors, or areas for improvement within the provided code. Once identified, you'll provide a bug report and offer fixed code snippets in a text area"},
                {"role": "user", "content": prompt}
            ]
    )

    sl.write(response.choices[0].message.content)