from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv


load_dotenv()

def generate_pet_name(animal_type):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
    )
    system_prompt = SystemMessage(content=f"You are a creative and friendly  pet name generator. Your only task is to suggest five cool names for the pets. Do not include any conversation or explanation in your final output, just the names.")
    human_message = HumanMessage(content=f"I have a {animal_type} and I need a pet name for it. Please suggest five cool names.")
    response = model.invoke([system_prompt, human_message])
    return response.content


if __name__ == "__main__":
    print(generate_pet_name("rat"))
