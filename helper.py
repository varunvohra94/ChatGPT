import os
import openai
from settings import CHAT_GPT_MODEL, TEMPERATURE

openai.api_key  = os.getenv('OPENAI_API_KEY')

CHAT_GPT_MODEL = "gpt-3.5-turbo"

def get_completion(prompt, model=CHAT_GPT_MODEL):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=TEMPERATURE, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=TEMPERATURE, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]