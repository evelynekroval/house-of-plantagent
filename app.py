"""
Streamlit interface for the House of PlantAgent.

This module demonstrates:
1. Session state management (Streamlit pattern for persistent data across reruns)
2. Agent streaming with real-time UI updates
3. Error handling for tool execution
4. User tracking with unique IDs and conversation threads

Key learning: Streamlit reruns the entire script on every interaction.
`st.session_state` is the only way to preserve data across reruns.
"""

import streamlit as st
import uuid
import os
from dotenv import load_dotenv

# Import agent components from src/
# Note: These imports trigger module-level code (agent initialization).
# We'll cache the agent to avoid re-instantiation on every Streamlit rerun.
from src.agent import agent, Context
from src.tools import scrying_the_skies

# Load environment variables before any external API calls
load_dotenv()

# ──────────────────────────────────────────────────────────────────────────────
# STREAMLIT PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="House of PlantAgent",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ──────────────────────────────────────────────────────────────────────────────
# SESSION STATE INITIALIZATION
# ──────────────────────────────────────────────────────────────────────────────
# Streamlit reruns the entire script on every interaction (button click, form submit, etc.).
# `st.session_state` is a dict that persists across reruns within a single browser session.
# This is essential for maintaining conversation history and user context.

def initialize_session_state():
    """Initialize session state variables if they don't exist.
    
    This is called once per session; subsequent calls skip initialization
    because Streamlit only initializes missing keys.
    """
    if "user_id" not in st.session_state:
        # Generate a unique ID for this user/session.
        # In a production app, you'd pull this from auth (Firebase, etc.).
        st.session_state.user_id = str(uuid.uuid4())
    
    if "thread_id" not in st.session_state:
        # Thread ID groups messages into a conversation.
        # The agent uses this for checkpointing and history.
        st.session_state.thread_id = str(uuid.uuid4())
    
    if "messages" not in st.session_state:
        # Local message log for display.
        # Format: [{"role": "user"|"assistant", "content": str}, ...]
        st.session_state.messages = []
    
    if "agent_thinking" not in st.session_state:
        # Flag to show when the agent is processing (UI feedback).
        st.session_state.agent_thinking = False

initialize_session_state()

# ──────────────────────────────────────────────────────────────────────────────
# UI: HEADER & DESCRIPTION
# ──────────────────────────────────────────────────────────────────────────────
st.title("🌿 House of :green[PlantAgent]")
st.markdown(
    """
    *Eleanor of Aquitane guides your vegan culinary journey.*
    
    Ask for a recipe, and I shall scry the skies to find the finest vegan dish for you.
    """
)

# Optional: Show user session info in sidebar
with st.sidebar:
    st.markdown("### Session Info")
    st.caption(f"User ID: `{st.session_state.user_id[:8]}...`")
    st.caption(f"Thread ID: `{st.session_state.thread_id[:8]}...`")
    
    if st.button("Clear History"):
        st.session_state.messages = []
        st.rerun()

# ──────────────────────────────────────────────────────────────────────────────
# UI: MESSAGE HISTORY DISPLAY
# ──────────────────────────────────────────────────────────────────────────────
# Render all previous messages in the conversation.
# st.chat_message() is a convenience container that styles messages like a chat UI.
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ──────────────────────────────────────────────────────────────────────────────
# UI: INPUT FORM
# ──────────────────────────────────────────────────────────────────────────────
# st.form() is critical: it prevents Streamlit from rerunning on every keystroke.
# Instead, the script only reruns when you click the submit button.
# Without this, every keystroke would trigger a full agent call—very expensive!

with st.form(key="recipe_form", clear_on_submit=True):
    user_input = st.text_input(
        "Ask for a recipe:",
        placeholder="e.g., 'Easy tofu and noodle recipe', 'High-protein Buddha bowl'",
    )
    submitted = st.form_submit_button("Search recipe")

# ──────────────────────────────────────────────────────────────────────────────
# AGENT EXECUTION
# ──────────────────────────────────────────────────────────────────────────────
if submitted and user_input.strip():
    # Add user message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # # Display user message immediately
    # with st.chat_message("user"):
    #     st.markdown(user_input)
    
    # Prepare agent call parameters
    # The config dict tells the agent which thread to use (for multi-turn conversations).
    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    
    # Context includes metadata about this user (for logging, personalization, etc.).
    context = Context(user_id=st.session_state.user_id)
    
    # Create a placeholder for the assistant's response.
    # We'll update this as the agent streams chunks.
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        status_placeholder = st.empty()
        
        agent_response = ""
        tool_calls_made = []
        
        try:
            # Stream agent response in real-time.
            # stream_mode="values" yields the full state at each step.
            for chunk in agent.stream(
                {
                    "messages": [{"role": "user", "content": user_input}]
                },
                context=context,
                stream_mode="values",
                config=config,
            ):
                # Extract the latest message from the agent's state.
                # The agent processes messages in chunks; we want the most recent one.
                latest_msg = chunk["messages"][-1]
                
                # Case 1: Agent generated text content
                if latest_msg.content:
                    agent_response = latest_msg.content
                    response_placeholder.markdown(agent_response)
                
                # Case 2: Agent is making tool calls (e.g., searching for recipes)
                elif latest_msg.tool_calls:
                    # Extract tool names for display
                    tools_called = [tc.get("name", "unknown") for tc in latest_msg.tool_calls]
                    tool_calls_made.extend(tools_called)
                    
                    # Show a status message so the user knows something is happening
                    with status_placeholder.container():
                        st.info(f"🔍 Searching: {', '.join(tools_called)}")
            
            # Clear the status message once complete
            status_placeholder.empty()
        
        except Exception as e:
            # Tool execution error or other agent failure.
            # This is critical for debugging and user feedback.
            st.error(f"⚠️ Eleanor encountered an error: {str(e)}")
            agent_response = f"Error: {str(e)}"
            
            # Log the error for debugging (in production, send to a monitoring service)
            print(f"[ERROR] User: {user_input}")
            print(f"[ERROR] Exception: {e}")
    
    # Add the agent's response to conversation history for future reruns
    st.session_state.messages.append({"role": "assistant", "content": agent_response})

# ──────────────────────────────────────────────────────────────────────────────
# OPTIONAL: DEBUG MODE
# ──────────────────────────────────────────────────────────────────────────────
# Show session state for debugging (disable in production)
if st.secrets.get("debug_mode", False):
    with st.expander("🐛 Debug: Session State"):
        st.write({
            "user_id": st.session_state.user_id,
            "thread_id": st.session_state.thread_id,
            "message_count": len(st.session_state.messages),
        })