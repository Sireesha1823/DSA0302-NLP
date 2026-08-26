from transformers import pipeline

# Load a text generation model
generator = pipeline("text-generation", model="distilgpt2")

# Get prompt from user
prompt = input("Enter your prompt: ")

# Generate text
result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
)

# Display generated text
print("\nGenerated Text")
print("----------------------------")
print(result[0]["generated_text"])