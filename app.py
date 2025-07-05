import streamlit as st
from components.prompt_input import render_prompt_input
from components.response_display import render_response_display
from components.notes_panel import render_notes_panel
from llms.gpt import get_gpt_response
from llms.gemini import get_gemini_response

# ✅ Set Streamlit page config
st.set_page_config(page_title="LLM Notes Taker", layout="wide")

# ✅ Initialize chat history if not already set
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Page Title
st.title("🧠 Multi-LLM Notes & Comparison Tool")

# ✅ Get user prompt
user_prompt = render_prompt_input()

# ✅ Get LLM responses if prompt is entered
# Inside your existing logic, after getting user_prompt
if user_prompt:
    # 🔁 Build stitched context from last prompt if available
    if len(st.session_state.chat_history) > 0:
        last_prompt = st.session_state.chat_history[-1]["prompt"]
        stitched_prompt = f"Previously I asked: '{last_prompt}'. Now: {user_prompt}"
    else:
        stitched_prompt = user_prompt

    with st.spinner("Querying GPT and Gemini..."):
        gpt_output = get_gpt_response(stitched_prompt)
        gemini_output = get_gemini_response(stitched_prompt)

    # Save the **original prompt**, not the stitched one
    st.session_state.chat_history.append({
        "prompt": user_prompt,
        "gpt": gpt_output,
        "gemini": gemini_output
    })


# ✅ Show all previous turns in chat history
st.subheader("🧾 Chat History")

for i, turn in enumerate(reversed(st.session_state.chat_history)):
    st.markdown(f"**Prompt {len(st.session_state.chat_history) - i}:** {turn['prompt']}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🔵 GPT Response:**")
        st.write(turn["gpt"])
    with col2:
        st.markdown("**🟢 Gemini Response:**")
        st.write(turn["gemini"])

    st.markdown("---")

# ✅ Notes section
render_notes_panel()

if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()
