def semantic_representation(query):
    query = query.lower()

    if "activate" in query and "roaming" in query:
        return "ACTIVATE(Roaming, Customer)"

    elif "deactivate" in query and "caller tune" in query:
        return "DEACTIVATE(CallerTune, Customer)"

    elif "check" in query and "data balance" in query:
        return "QUERY(DataBalance, Customer)"

    elif "enable" in query and "5g" in query:
        return "ACTIVATE(5GService, Customer)"

    elif "deactivate" in query:
        return "DEACTIVATE(Service, Customer)"

    elif "activate" in query or "enable" in query:
        return "ACTIVATE(Service, Customer)"

    else:
        return "UNKNOWN"

# Input
query = input("Enter customer query: ")

# Output
print("Semantic Representation:", semantic_representation(query))
