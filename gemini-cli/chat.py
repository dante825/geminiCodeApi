
import os
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

def main():
    """
    Main function to handle the chat interface.
    """
    load_dotenv(dotenv_path='gemini.env')
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    chat = model.start_chat(history=[])

    print("\nWelcome to Gemini Chat! Type 'exit' or press Ctrl+C to quit.\n")

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            
            response = chat.send_message(user_input)
            print(f"Gemini: {response.text}")

    except KeyboardInterrupt:
        print("\nExiting chat. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
