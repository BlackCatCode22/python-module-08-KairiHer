import streamlit as st
import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY") or st.text_input("Enter your OpenAI API key", type="password")


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]


st.markdown("<h1 style='text-align: center;'>🧠 Python Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)


user_input = st.text_input("You:", "")


if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=st.session_state.messages
        )

        reply = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")

# Display chat
st.markdown("### Conversation:")
for msg in st.session_state.messages[1:]: 
    speaker = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
    st.markdown(f"**{speaker}:** {msg['content']}")

