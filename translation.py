from google.cloud import translate_v2 as translate

def translate_to_english(text):
    """
    Translates the input text to English using Google Cloud Translation API.
    """
    client = translate.Client()
    result = client.translate(text, target_language="en")
    return result['translatedText']

def translation_repl():
    """
    A REPL loop for translating text into English.
    """
    print("Google Translate REPL")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter text to translate: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            translated_text = translate_to_english(user_input)
            print(f"Translated text: {translated_text}")
        except Exception as e:
            print(f"Error: {e}. Please ensure your API setup is correct.")

# Start the REPL
if __name__ == "__main__":
    translation_repl()
