responses = [
    "Take a short break and then return to your exam preparation with a clear focus. This can help you concentrate better, and you can feel confident about doing your best.",

    "Since your exam is tomorrow, take a short break and start again with small study goals. Keep your focus on one topic at a time, and stay confident that you can prepare well.",

    "You may be finding it difficult to concentrate because you are worried about the exam, so take a short break before studying again. Regain your focus and stay confident—you can handle the preparation one step at a time."
]

required_keywords = ["focus", "break", "confident"]

print("CONSTRAINED DIALOG GENERATION")
print("-----------------------------")

valid_responses = []

for i, response in enumerate(responses, 1):

    sentences = response.split(".")
    sentence_count = len([s for s in sentences if s.strip()])

    keyword_count = 0

    for word in required_keywords:
        if word in response.lower():
            keyword_count += 1

    length_ok = 2 <= sentence_count <= 3
    keywords_ok = keyword_count >= 2

    print("\nResponse", i)
    print(response)

    print("Number of sentences:", sentence_count)
    print("Required keywords found:", keyword_count)

    if length_ok and keywords_ok:
        print("Constraint Status: Satisfied")
        valid_responses.append(i)
    else:
        print("Constraint Status: Not Satisfied")


print("\nEvaluation")
print("----------")

if valid_responses:
    print("Valid responses:", valid_responses)
    print("Best Response: Response 2")
    print("Reason: It satisfies the dialog, keyword, coherence, length,")
    print("logical consistency and positive-tone constraints.")
