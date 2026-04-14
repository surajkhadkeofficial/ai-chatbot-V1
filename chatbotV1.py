from google import genai
from google.genai import types
import os 
from dotenv import load_dotenv


load_dotenv() 
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def chatfun(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text.strip()

if __name__=="__main__":
    while True:
        userinput=input("you : ")
        
        if userinput.strip().lower() in ["exit", "bye","end"]:
            print("Bye!")
            break
        else:
            response=chatfun(userinput)
            print(f"bot: {response}")

