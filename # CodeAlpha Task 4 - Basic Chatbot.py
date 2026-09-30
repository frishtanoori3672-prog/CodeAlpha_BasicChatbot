# CodeAlpha Task 4 - Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can have a simple conversation with you."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that yet."


print("=" * 45)
print("           BASIC CHATBOT")
print("=" * 45)

print("Hello! I am your simple Python chatbot.")
print("You can say hello, ask how I am, or say bye.")
print("Type 'bye' to end the conversation.")

while True:
    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "goodbye"]:
        break

print("\nChatbot session ended.")