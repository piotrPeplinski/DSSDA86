import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.environ['API_KEY']

question = 'How to use ENV variables in Python?'

client = OpenAI(api_key=API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": question
        }
    ]
)


print(response)