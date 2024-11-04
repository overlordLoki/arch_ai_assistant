# src/user_chat/chat.py

from src.brain.brain import process_message
frontend_conversation_history = []

def chat_loop():
    print("Hi! I'm a Artie. your AI Assistant! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        frontend_conversation_history.append({"role": "user", "content": user_input})
        if user_input.lower() == 'exit':
            print("Artie: Goodbye!")
            break
        response = process_message(user_input)
        frontend_conversation_history.append({"role": "assistant", "content": response})
        print(f"Artie: {response}")