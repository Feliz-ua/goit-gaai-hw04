import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# Завантажуємо .env, розташований поруч із цим скриптом.
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("Не знайдено OPENROUTER_API_KEY. Перевір файл .env.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    timeout=60.0,
    max_retries=0,
)

MODEL = "openai/gpt-oss-120b"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Відповідай лише одним словом: Працює",
        }
    ],
    temperature=0,
)

print("Модель:", response.model)
print("Відповідь:", response.choices[0].message.content)