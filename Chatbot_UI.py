import streamlit as st
import os

# Page configuration
def chat_interface(sql_chain):
    st.set_page_config(page_title="FinBot", layout="centered", initial_sidebar_state="auto")

    # Title and header
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>💸<b>Finance Bot</b>🤖 </h1>", unsafe_allow_html=True)

    # Initialize session state for conversation history and loading state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if "loading" not in st.session_state:
        st.session_state.loading = False



    # Defining containers for chat and input
    chat_container = st.container()
    input_container = st.container()

    # Display chat messages in the chat container
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(
                    f'<div style="background-color:#DCF8C6; padding:10px; border-radius:10px; margin:10px 0; text-align:left; display:flex; align-items:center;">'
                    f'<span style="font-size:1.5em; margin-right:10px;">👤</span>'
                    f'<div>{msg[ "content" ]}</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div style="background-color:#E1E1E1; padding:10px; border-radius:10px; margin:10px 0; text-align:left; display:flex; align-items:center;">'
                    f'<span style="font-size:1.5em; margin-right:10px;">🤖</span>'
                    f'<div>{msg[ "content" ]}</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )


        # Display loading spinner if the bot is generating a response
        if st.session_state.loading:
            with st.spinner("Thinking..."):
                pass
        st.markdown('</div>', unsafe_allow_html=True)

    # Input box for user queries
    with input_container:
        query = st.chat_input(placeholder="Ask your question here...")

        if query:
            # Store the user's message
            st.session_state.messages.append({"role": "user", "content": query})
            st.session_state.loading = True

            # Simulating bot response logic here
            def get_bot_response():
                try:
                    # Simulating a bot response for demo purposes
                    bot_response = sql_chain.run(query)

                    # Store the bot's response
                    st.session_state.messages.append({"role": "bot", "content": bot_response})
                except Exception as e:
                    # Handle errors
                    st.error(f"An error occurred: {str(e)}")
                finally:
                    # Turn off the loading spinner
                    st.session_state.loading = False
                    # Rerun to update the UI
                    st.rerun()

            # Call the function to get the bot response
            get_bot_response()


# Run the chat interface
# if __name__ == "__main__":
#     chat_interface()
