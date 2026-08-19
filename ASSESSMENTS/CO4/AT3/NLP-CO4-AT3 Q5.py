sentence = "The boy eats an apple"
print("Original Sentence:")
print(sentence)
print()
print("===== TRANSITION-BASED PARSING =====")
words = ["The", "boy", "eats", "an", "apple"]
stack = []
buffer = words.copy()
print("Initial Stack:", stack)
print("Initial Buffer:", buffer)
print()
while len(buffer) > 0:
    word = buffer.pop(0)
    stack.append(word)
    print("SHIFT ->", word)
    print("Stack :", stack)
    print("Buffer:", buffer)
    print()
print("Transition-Based Parsing Completed.")
print()
print("===== TRANSITION DEPENDENCIES =====")
print("eats -> subject -> boy")
print("eats -> object -> apple")
print("boy -> determiner -> The")
print("apple -> determiner -> an")
print()
print("===== GRAPH-BASED PARSING =====")
dependencies = [
    ("eats", "boy", "subject"),
    ("eats", "apple", "object"),
    ("boy", "The", "determiner"),
    ("apple", "an", "determiner")
]
print("Dependency Graph:")
print()
for head, dependent, relation in dependencies:
    print(head, "--", relation, "-->", dependent)
print()
print("===== GRAPH STRUCTURE =====")

print("             eats")
print("            /    \\")
print("      subject    object")
print("        /          \\")
print("      boy          apple")
print("      /             /")
print(" determiner     determiner")
print("    /               /")
print("   The             an")

print()
print("===== COMPARISON =====")

print("Transition-Based Parsing:")
print("1. Makes decisions step by step.")
print("2. Processes the sentence sequentially.")
print("3. It is generally fast.")
print("4. It is suitable for large datasets.")

print()

print("Graph-Based Parsing:")
print("1. Represents dependencies as a graph.")
print("2. Considers possible relationships.")
print("3. Selects the best dependency structure.")
print("4. Provides global structural analysis.")

print()
print("===== RESULT =====")

print("Transition-based parsing is suitable")
print("for large-scale applications because")
print("it provides fast sequential processing.")

print()

print("Graph-based parsing considers the")
print("overall dependency structure and")
print("provides global analysis.")
