from transformers import pipeline

# Load a free LLM (Falcon)
generator = pipeline("text-generation", model="distilgpt2")

def get_llm_response(prompt):
    result = generator(prompt, max_length=300, num_return_sequences=1)
    return result[0]['generated_text']
