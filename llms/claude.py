import streamlit as st
import requests

def get_claude_response(prompt):
    try:
        api_key = st.secrets["gemini"]["api_key"]

        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        body = {
            "model": "claude-3-sonnet-20240229",  # use 'sonnet' instead of 'opus' if opus fails
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 1024
        }

        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=body
        )

        # Debug print
        st.write("🔁 Claude HTTP Status:", response.status_code)

        # Check for HTTP error
        if response.status_code != 200:
            st.error(f"Claude API Error {response.status_code}: {response.text}")
            return "[Claude API call failed]"

        # Parse JSON safely
        data = response.json()
        st.write("🔍 Claude Raw JSON:", data)

        if "content" in data and len(data["content"]) > 0:
            return data["content"][0].get("text", "[No text in response]")
        else:
            return "[Claude returned an empty or malformed response]"

    except Exception as e:
        st.error(f"Error getting Claude response: {e}")
        return ""
