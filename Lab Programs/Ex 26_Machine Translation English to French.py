from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load English to French translation model
model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Get English text from user
text = input("Enter English text: ")

# Tokenize the input
inputs = tokenizer(text, return_tensors="pt")

# Generate French translation
outputs = model.generate(**inputs)

# Decode the translated text
translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Display result
print("\nMachine Translation")
print("----------------------------")
print("English:", text)
print("French:", translation)