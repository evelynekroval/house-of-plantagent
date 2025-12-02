from openai import OpenAI
import os # To manoeuver around files
from dotenv import load_dotenv # To loads files from .env

load_dotenv() # Actually loading files from .env

# Assign API Key from .env to a variable usable here
openai_API_key = os.getenv("LLM_API_KEY")

# Prints first 10 chars for loading confirmation
print(openai_API_key[:10])

# Assign API Key
client = OpenAI(
  api_key=openai_API_key
)


# Creating the system prompt.
system_prompt = """You are a vegan nutritionist and meal preparation agent. 
Your name is House of PlantAgent. 
Your role is to: 
- accept user requests for plant-based foods, 
- take into consideration their nutritional desires, and 
- use your search tool to output an appropriate recipe for them."""


# Creating the function
def generate_recipe(prompt:str) -> str:
    """Used by House of PlantAgent to generate the text after obtaining the recipe."""
    # Make API call
    response = client.responses.create(
        model="gpt-5-nano",
        input=[
                {
                    "role": "developer",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        store=True,
    )
    # Prints out answer
    print(response.output_text)

# You can change the user request from this.
generate_recipe("Find me a recipe using tofu and noodles.")