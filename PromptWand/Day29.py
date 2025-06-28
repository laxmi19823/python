import random
import json
from datetime import datetime
import os

# Load prompts from JSON
def load_prompts():
    filename = r"C:\Users\laxmi\OneDrive\Desktop\30\Day29\writing_prompts.json"
    
    if not os.path.exists(filename):
        print(f"❌ File not found at: {filename}")
        print("💡 Make sure 'writing_prompts.json' is placed in the correct folder.")
        return None
    
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Save prompt to text file
def save_prompt(prompt):
    with open("writing_prompts.txt", "a", encoding='utf-8') as f:
        f.write(f"{datetime.now()}: {prompt}\n\n")

# Main
def run():
    data = load_prompts()
    if data is None:
        return  # Stop execution if loading failed

    print("Choose a category:", ", ".join(data.keys()))
    category = input("Enter category: ").lower()

    if category in data:
        prompt = random.choice(data[category])
        print(f"\n✨ Your prompt:\n{prompt}\n")
        save_prompt(prompt)
    else:
        print("❌ Invalid category.")

if __name__ == "__main__":
    run()