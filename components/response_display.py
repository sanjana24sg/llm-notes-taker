import streamlit as st

def render_response_display(gpt_output, claude_output):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔵 GPT Output")
        st.write(gpt_output)

    with col2:
        st.subheader("🟡 Gemini Output")
        st.write(claude_output)
