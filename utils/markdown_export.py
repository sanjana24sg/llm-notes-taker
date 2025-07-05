import streamlit as st

def export_to_md(text):
    st.download_button(
        label="Download Markdown",
        data=text,
        file_name="llm_notes.md",
        mime="text/markdown"
    )
