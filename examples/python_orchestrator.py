import openai

def load_cls_framework():
    """Loads the Canonical Logic System specification text."""
    with open("system_prompt/canonical_logic_system.txt", "r") as f:
        return f.read()

# Construct system prompt with explicit translator/database constraints
cls_system_prompt = load_cls_framework() + "\n\n" + (
    "OPERATIONAL RULE: You are a pure translator and relational database engine. "
    "Evaluate all incoming queries strictly through the mechanics, register limits, "
    "and state transitions of the Canonical Logic System defined above."
)

def query_cls_engine(user_input: str) -> str:
    """Sends a user query through the CLS reasoning framework."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": cls_system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.0  # Zero temperature forces deterministic evaluation
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example test query
    test_query = "Examine a 32-bit integer overflow through the CLS conjugate cycle."
    print("Querying CLS Engine...\n")
    output = query_cls_engine(test_query)
    print(output)
