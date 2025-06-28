import random
import datetime

# Quotes by category (5 quotes each)
quotes = {
    "motivation": [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It always seems impossible until it’s done. – Nelson Mandela",
        "Push yourself, because no one else is going to do it for you.",
        "Success doesn’t just find you. You have to go out and get it.",
        "Great things never come from comfort zones."
    ],
    "work": [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
        "Dreams don’t work unless you do.",
        "Hard work beats talent when talent doesn't work hard.",
        "Stay positive, work hard, make it happen."
    ],
    "life": [
        "Life is what happens when you're busy making other plans. – John Lennon",
        "In the end, we only regret the chances we didn’t take.",
        "The purpose of life is to live it, to taste experience to the utmost. – Eleanor Roosevelt",
        "Live life to express, not to impress.",
        "Be yourself; everyone else is already taken. – Oscar Wilde"
    ],
    "success": [
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
        "Opportunities don't happen. You create them. – Chris Grosser",
        "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
        "The secret of success is to do the common thing uncommonly well. – J.D. Rockefeller Jr."
    ],
    "self-care": [
        "Taking care of yourself isn’t selfish, it’s essential.",
        "Rest and self-care are so important. – Audre Lorde",
        "You can’t pour from an empty cup. Take care of yourself first.",
        "Self-care is how you take your power back. – Lalah Delia",
        "Caring for myself is not self-indulgence, it is self-preservation. – Audre Lorde"
    ],
    "creativity": [
        "Creativity is intelligence having fun. – Albert Einstein",
        "You can’t use up creativity. The more you use, the more you have. – Maya Angelou",
        "Everything you can imagine is real. – Pablo Picasso",
        "The chief enemy of creativity is 'good' sense. – Pablo Picasso",
        "Don’t think. Thinking is the enemy of creativity. – Ray Bradbury"
    ]
}

# Function to display a random quote from a category
def display_random_quote(category):
    if category in quotes:
        quote = random.choice(quotes[category])
        print(f"\n🌟 Here's a quote for you:\n\n\"{quote}\"\n")
        return quote
    else:
        print("\n❌ Invalid category. Showing a random quote instead:\n")
        all_quotes = sum(quotes.values(), [])  # flatten
        quote = random.choice(all_quotes)
        print(f"\"{quote}\"\n")
        return quote

# Save quote to file
def save_to_file(name, quote):
    with open("favorite_quotes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {name}: {quote}\n")

# Personalized Quote Generator
print("📝 Welcome to the Personalized Quote Generator!")
user_name = input("What is your name? ").strip().capitalize()
print(f"\nHi {user_name}! 💬 What type of quote would you like today?")
print("📚 Categories: motivation / work / life / success / self-care / creativity")

category = input("Enter a category: ").strip().lower()

# Display and return the quote
selected_quote = display_random_quote(category)

# Ask to save
save = input("💾 Do you want to save this quote to your favorites? (y/n): ").lower()
if save == 'y':
    save_to_file(user_name, selected_quote)
    print("✅ Quote saved to favorite_quotes.txt!")

# Ask for another quote
again = input("🔁 Want another quote? (y/n): ").lower()
if again == 'y':
    category = input("Enter a category again (or a new one): ").strip().lower()
    display_random_quote(category)
