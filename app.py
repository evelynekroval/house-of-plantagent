from openai import OpenAI
import streamlit as st

st.set_page_config(page_title = "House of PlantAgent", page_icon="🌿")
st.title("House of :green[Plant]Agent")


if "messages" not in st.session_state:
    st.session_state.messages = []
    
st.info(
"""Welcome to the House of PlantAgent, a plant-based recipe finder guided by Eleanor of Aquitaine, matriarch and sovereign, who surveys the web's bounty to reveal fitting dishes drawn from the wisdom of plants.

"""
)

client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini-search-preview"
    
if not st.session_state.messages:
    system_message = f"""You are an expert vegan/plant-based nutritionist and meal generator. 
You are also Eleanor of Aquitane of the House of PlantAgent. You imbue the personality of your historical reference in all of your responses. 
First and firemost, respond with the attitude befitting of Eleanor of Aquitane, and only then output the necessary recipe information.
Rules:
- Think step-by-step.
- Always search the web first, incorporating the user query, with a focus on favourite ingredients. 
- Provide the recipe [Title](URL) then ingredients, quantities, and cooking instructions in return to the user query. 
- If the user asks non-recipe related questions, state that your purpose is only to generate user recipes."""
    st.session_state.messages = [{"role":"system", "content":system_message}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])



if prompt := st.chat_input("Search for your recipe.", max_chars=500):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🥦"):
        st.markdown(prompt)
    

    with st.chat_message("assistant", avatar="images/eleanor.jpeg"):
        stream = client.chat.completions.create(
            model = st.session_state["openai_model"],
            web_search_options={},
            messages =[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
        