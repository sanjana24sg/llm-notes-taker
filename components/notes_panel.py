import streamlit as st
from utils.markdown_export import export_to_md

def render_notes_panel():
    st.subheader("📝 Your Notes")
    notes = st.text_area("Write your summary or observations here:")
    
    if st.button("📥 Export Notes as Markdown"):
        export_to_md(notes)
