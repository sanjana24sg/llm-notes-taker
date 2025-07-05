import streamlit as st
import requests

def get_gemini_response(prompt):
    try:
        api_key = st.secrets["gemini"]["api_key"]

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key
        }

        body = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=body)

        if response.status_code != 200:
            st.error(f"Gemini API error {response.status_code}: {response.text}")
            return "[Gemini API failed]"

        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        st.error(f"Error calling Gemini: {e}")
        return ""
