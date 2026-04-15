# generate_data.py

import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_synthetic_queries(base_query):
    prompt = f"""
    Generate 10 different variations of the following query.

    Return them as a numbered list.

    Query: {base_query}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You generate test queries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    text = response.choices[0].message.content

    # For debugging
    # print("=="*40)
    # print(text)
    # print("=="*40)
    
    queries = [line.split(". ", 1)[1] for line in text.split("\n") if ". " in line]
    
    return queries

def save_to_csv(queries):
    df = pd.DataFrame({"query": queries})
    df.to_csv("data/synthetic_queries.csv", index=False)

if __name__ == "__main__":
    base_queries = [
    "What is your refund policy?",
    "How do I contact support?",
    "Can I upgrade my plan?"
    ]

    all_queries = []
    
    for base in base_queries:
        generated = generate_synthetic_queries(base)
        all_queries.extend(generated)

    save_to_csv(all_queries)
    
    print("Saved synthetic queries to CSV.")

# Run:
# python data/generate_data.py