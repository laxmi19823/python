import json
import random
from datetime import datetime

# 📁 Writing prompt collection
prompts_json = {
    "poetry": [
        "Write a poem about the last light of dusk.",
        "Describe love as if it were a forgotten language.",
        "Write a haiku about silence.",
        "Personify the moon watching over a sleeping city.",
        "Write a poem that starts with 'If only I could fly…'"
    ],
    "sci-fi": [
        "A robot gains consciousness—describe its first emotion.",
        "Humans discover a new planet with ancient ruins—write the log entry.",
        "The year is 3025, and dreams are government property.",
        "Aliens offer to fix Earth, but in return, they want something unexpected.",
        "Time travel is outlawed, but you just received a letter from your future self."
    ],
    "fantasy": [
        "A dragon is tired of guarding treasure and wants a new job.",
        "Describe a kingdom where magic is powered by music.",
        "A child finds a glowing key in the forest—what does it unlock?",
        "A forgotten god awakens in a small village.",
        "The royal heir runs away to become a wandering bard."
    ],
    "life": [
        "Write about a time you felt truly free.",
        "Describe a simple moment that changed your life forever.",
        "You meet your childhood self in a dream—what do you say?",
        "Write a letter to someone who changed your life without knowing it.",
        "Capture the feeling of coming home after a long journey."
    ]
}

# 🎯 Pick a random category and prompt
category = random.choice(list(prompts_json.keys()))
prompt = random.choice(prompts_json[category])
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 📝 Format output line
output_line = f"{timestamp} [{category}] {prompt}"

# 💾 Save to file
with open("prompts_log.txt", "a") as file:
    file.write(output_line + "\n")

print("Prompt saved! ✨") 