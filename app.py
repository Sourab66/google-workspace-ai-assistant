
import streamlit as st
import requests

st.title("Your Personal Assistant")

st.subheader("What can your personal assistant do?")

st.markdown("""
1. Answer questions on various topics.
2. Arrange Calendar events and meetings.
3. Read your emails and send replies, can even summarize them for you.
4. Manage your tasks and to-do lists.
5. Take quick notes for you.
6. Track your expenses and budgeting.
""")

st.subheader("💬 Chat with your assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_message = st.chat_input("Type your message")

if user_message:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)

    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    try:
        # Send request to n8n webhook
        response = requests.post(
            "https://n8n.sketch2garment.shop/webhook-test/947c59ca-cd42-4678-ab3b-e2a43a7bcf09",
            json={"message": user_message},
            timeout=60
        )

        # Extract AI response
        data = response.json()

        if isinstance(data, list):
         ai_response = data[0].get("output", str(data))
        elif isinstance(data, dict):
         ai_response = data.get("output", str(data))
        else:
         ai_response = str(data)

    except Exception as e:
        ai_response = f"Error: {e}"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )
