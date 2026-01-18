import streamlit as st
from groq import Groq


client=Groq(api_key="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")
def ask_ai(prompt):
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[{"role":"user","content":prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content

st.markdown("<style> .stApp { background-color: #8B00FF  } </style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; font-size: 40px;'>AI Study Buddy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Your personal AI study assistant</p>", unsafe_allow_html=True)



option = st.selectbox(
    "Select a feature:",
    ["Explain Topic","Summarize Notes","Generate Quiz"]
)
text=st.text_area("Enter your topic or notes here:")


if st.button("Run"):
    if not text.strip():
        st.warning("Please enter some text")
    else:
        if option == "Explain Topic":
            result = ask_ai(f"Explain this in simple terms: {text}")
        elif option == "Summarize Notes":
            result = ask_ai(f"Summarize this text: {text}")
        elif option == "Generate Quiz":
            result = ask_ai(f"Create 5 quiz questions with answers from this text: {text}")
        st.success(result)
