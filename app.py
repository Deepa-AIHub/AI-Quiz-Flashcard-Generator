
import streamlit as st
import ollama

st.set_page_config(page_title="AI Quiz Generator",
                   page_icon="🧠")

st.title("🧠 AI Quiz Generator")
st.write("Turn your study notes into a quiz!")

notes = st.text_area(
    "Enter your study notes:",
    height=200,
    placeholder="Paste your Python or AI notes here..."
)

if st.button("Generate Quiz"):
    if not notes.strip():
        st.warning("Please enter your notes first.")
    else:
        with st.spinner("AI is creating your quiz..."):
            prompt = f"""
            Create 5 multiple-choice questions
            based ONLY on these study notes.

            For each question:
            - Give 4 options (A, B, C, D)
            - Identify the correct answer
            - Explain the answer briefly

            Study notes:
            {notes}
            """

            try:
                response = ollama.generate(
                    model="llama3.2",
                    prompt=prompt
                )

                st.subheader("Your AI-generated quiz")
                st.write(response["response"])

            except Exception as e:
                st.error(f"Error: {e}")