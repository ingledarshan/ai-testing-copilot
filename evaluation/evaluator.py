# evaluator.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_response(query, ai_response):
    prompt = f"""
        Evaluate the response strictly.

        Give scores from 1 to 5 for:
        1. Relevance
        2. Correctness
        3. Completeness

        Return in this format:

        Relevance: <score>
        Correctness: <score>
        Completeness: <score>
        Final Score: <average>
        Reason: <short explanation>

        Query: {query}
        Response: {ai_response}
        """

    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a strict evaluator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return result.choices[0].message.content
