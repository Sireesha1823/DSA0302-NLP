import re

# Function to recognize dialog act
def recognize_dialog_act(sentence):
    text = sentence.lower().strip()

    # Greeting
    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Greeting"

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye", "see you", "good night"]):
        return "Goodbye"

    # Question
    elif text.endswith("?") or text.startswith(
        ("what", "why", "when", "where", "who", "how", "can", "could", "do", "does", "is", "are")
    ):
        return "Question"

    # Request
    elif any(word in text for word in ["please", "request", "would you", "could you"]):
        return "Request"

    # Thanking
    elif any(word in text for word in ["thank you", "thanks", "thank"]):
        return "Thanking"

    # Agreement
    elif any(word in text for word in ["yes", "okay", "sure", "correct", "right"]):
        return "Agreement"

    # Apology
    elif any(word in text for word in ["sorry", "apologize", "apologies"]):
        return "Apology"

    # Default
    else:
        return "Statement"


# Input conversation
print("Enter the dialog line.")
sentence = input("User: ")

# Recognize dialog act
dialog_act = recognize_dialog_act(sentence)

# Display result
print("\nDialog Act Recognition")
print("----------------------------")
print("Input:", sentence)
print("Dialog Act:", dialog_act)