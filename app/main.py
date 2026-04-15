# main.py
from evaluation.evaluator import evaluate_response

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(user_query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional customer support agent. Always give accurate and policy-based answers."},
            {"role": "user", "content": user_query}
        ],
        temperature=0.7 # 0.7 keep the creativity on a little higher side
    )
    return response.choices[0].message.content

# if __name__ == "__main__":
#     query = input("Enter your query: ")
#     answer = get_ai_response(query)
#     print("\nAI Response:\n", answer)

query = "What is your refund policy?"
answer = get_ai_response(query)

print("AI Response:\n", answer)

evaluation = evaluate_response(query, answer)
print("\nEvaluation:\n", evaluation)

# Run the app:
# touch evaluation/__init__.py
# python -m app.main