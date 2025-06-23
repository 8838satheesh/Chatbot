import openai
import os
from chunking import chunk_text, get_relevant_chunks

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def get_answer(query, text_source):
    chunks = chunk_text(text_source)
    relevant = get_relevant_chunks(chunks, query)
    prompt = f"You are a helpful assistant for Tamil Nadu colleges. Use the following info:\n{''.join(relevant)}\n\nAnswer: {query}"
    return ask_llm(prompt)
