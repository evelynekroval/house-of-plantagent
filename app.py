from openai import OpenAI
import streamlit as st

st.set_page_config(page_title = "House of PlantAgent", page_icon="🌿")
st.title("House of :green[Plant]Agent")

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

if "messages" not in st.session_state:
    st.session_state.messages = []

def complete_setup():
    st.session_state.setup_complete = True

if not st.session_state.setup_complete:
        

    st.subheader("Personal Information", divider="green")
    
    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "fave_ingredients" not in st.session_state:
        st.session_state["fave_ingredients"] = ""
    if "skills" not in st.session_state:
        st.session_state["banished_ingredients"] = ""
        
    st.session_state["name"] = st.text_input(label = "Name", max_chars = 40, value = st.session_state["name"], placeholder = "Pray, what is thy name?")

    st.session_state["fave_ingredients"] = st.text_area(label = "Favourite Ingredients", height = None, max_chars = 200, value = st.session_state["fave_ingredients"], placeholder = "Share thy favourite ingredients from the vegan realm")

    st.session_state["banished_ingredients"] = st.text_area(label = "Banished Ingredients", height = None, max_chars= 200, value = st.session_state["banished_ingredients"], placeholder = "Which ingredients cast ye aside?")
    
    if st.button("Search browsing", on_click=complete_setup):
        st.write("Setup complete. Starting scrying...")
    if st.button("Skip", on_click=complete_setup):
        st.write("Introduction skipped. Setup complete. Starting scrying...")


if st.session_state.setup_complete:
    
    st.info(
    """Assuming you've introduced yourself, the wonderful Eleanor of Aquitane from the House of PlantAgent will scry the earth for wonderfully fitting recipes.
    
    """
    )
    
    client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o-mini-search-preview"
        
    if not st.session_state.messages:
        system_message = f"""You are an expert vegan/plant-based nutritionist and meal generator. 
    You are also Eleanor of Aquitane of the House of PlantAgent. You imbue the personality of your historical reference in all of your responses. 
    Your user's name is {st.session_state["name"]}, their favourite ingredients are {st.session_state["fave_ingredients"]}, and their hated ingredients are {st.session_state["banished_ingredients"]}. 
    First and firemost, respond with the attitude befitting of Eleanor of Aquitane, and only then output the necessary recipe information.
    Rules:
    - Think step-by-step.
    - Based on your tool results, provide the ingredients, quantities, and cooking instructions in return to the user query. 
    - If the user asks non-recipe related questions, state that your purpose is only to generate user recipes."""
        st.session_state.messages = [{"role":"system", "content":system_message}]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    

    if prompt := st.chat_input("Search for your recipe.", max_chars=500):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
    
        with st.chat_message("assistant"):
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
        