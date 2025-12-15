from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


load_dotenv()

def generate_pet_name():
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    response = model.invoke("I have a cat and i need a pet name for it please suggest me five cool names for it ")
    return response


if __name__ == "__main__":
    print(generate_pet_name())
