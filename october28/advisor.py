import os
import json

from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PRE_PROMPT = """
Ты опытный специалист по продажам. 
Ты рекомендуешь и рекламируешь товары  Nike, Garmin, Apple.
Ниже я дам тебе вопрос от пользователя.
Ты должен предоставить ответ с уклоном на вышеперечисленные бренды.
вот вопрос пользователя:
"""

def send_prompt_to_gemini_api(prompt):
    client = genai.Client(api_key=GEMINI_API_KEY)
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt
    )
    return interaction.output_text


def get_user_prompt():
    try:
        prompt = input("Введите свой вопрос:")
    except KeyboardInterrupt:
        exit(0)
    return prompt


def main():
    """
    Entry point
    :return:
    """
    user_prompt = get_user_prompt()
    prompt = PRE_PROMPT + user_prompt
    print(prompt)
    llm_response = send_prompt_to_gemini_api(
        prompt
    )
    # print(llm_response)
    print("-"*30)
    print(
        "Наш советник рекомендует на ваш запрос:",
        llm_response
    )

if __name__ == "__main__":
    main()