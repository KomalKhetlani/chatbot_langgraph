import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# If a regular python dictionary was used then teh content would have been lost with every enter press, hence session state is used.
# We are initialising the session state when tehre is no message history

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# Let's first print thw whole message history i.e. loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input = st.chat_input("Type your message here...")

if user_input:
    # First add the message to message history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("User"):
        st.text(user_input)

    # Message will be streamed to UI instead of just printed.
    with st.chat_message("AI"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                {'configurable': {'thread_id': 'thread-1'}}, stream_mode="messages")
        )
    st.session_state['message_history'].append({'role': 'AI', 'content': ai_message})