import streamlit as st
from openai import OpenAI

def get_gpt_response(prompt):
    try:
        client = OpenAI(api_key=st.secrets["openai"]["api_key"])

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error getting GPT response: {e}")
        return ""
