
import datetime
import time

# Time-based greeting
name = input("Enter your name: ")
present_time = datetime.datetime.now().hour

if 5 <= present_time < 11:
    print(f"Good morning {name}")
elif 11 <= present_time < 17:
    print(f"Good afternoon {name}")
elif 17 <= present_time < 20:
    print(f"Good evening {name}")
else:
    print(f"Good night {name}")

print("\nWelcome to your chatbot!")
print("You can ask me basic questions. Type 'bye' to exit.\n")

# responses dictionary
responses = {
    "hello": "Hi, welcome. How can I help you? :)",
    "how are you": "I am fine, thank you!",
    "who are you": "I am a simple rule-based AI chatbot.",
    "happy": "Great to hear that :D",
    "yo i have question for you": "Shoot!",
    "what is your name": "I don't exist in real life, but you can give me a name if you like."
}

def get_response(user_question: str) -> str:
    user_question = user_question.lower()

    if "sad" in user_question:
        return "I feel sorry to hear that :( I hope things get better soon."
    if "happy" in user_question:
        return "I feel good to hear that :) Keep smiling!"

    for key in responses:
        if key in user_question:
            response = responses[key]
            # emoji replacements
            response = response.replace(":)", "😊")
            response = response.replace(":(", "☹️")
            response = response.replace(":D", "😃")
            response = response.replace(";)", "😉")
            return response

    time.sleep(1)
    return "I am not capable of answering this particular question yet, but I'll learn."

# chat loop
while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "bye":
        print("Bot: Goodbye! Have a nice day 🙂")
        break

    reply = get_response(user_input)
    print("Bot:", reply)
