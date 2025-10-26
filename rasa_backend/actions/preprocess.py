# preprocess.py
import re

# Optional: define synonym mapping
SYNONYMS = {
    "artificial intelligence": "AI",
    "machine learning": "ML",
    "ml": "ML",
    "ai": "AI",
    "data analysis": "Data",
    "web development": "Web",
    "mobile development": "Mobile",
}

def clean_text(text: str) -> str:
    """
    Clean user input text:
    - Convert to lowercase
    - Remove special characters
    - Map synonyms to standard keywords
    """
    text = text.lower()  # lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # remove punctuation

    # Map synonyms
    for key, value in SYNONYMS.items():
        if key in text:
            text = text.replace(key, value)

    return text

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("Enter your interest: ")
        if user_input.lower() == "exit":
            break
        processed_input = clean_text(user_input)
        print(f"Processed input: {processed_input}")
