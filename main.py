import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Speech-to-Text using google's speech recognizer
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""

# Translation
def translate_text(text, target_language="de"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌍 Translated text: {translation.text}")
    return translation.text

# Language selection
def display_language_options():
    print("🌍 Available translation languages: ")
    print("1. German (de) - TEST LANGUAGE")
    print("2. Spanish (es) - TEST LANGUAGE")
    print("3. French (fr) - TEST LANGUAGE")
    print("4. English (en) - TEST LANGUAGE")
    print("5. Hindi (hi)")
    print("6. Tamil (ta)")
    print("7. Telugu (te)")
    print("8. Marathi (mr)")

    choice = input("Please select the target language number (1-8): ")
    language_dict = {
        "1": "de", "2": "es", "3": "fr", "4": "en",
        "5": "hi", "6": "ta", "7": "te", "8": "mr"
    }
    return language_dict.get(choice, "de")
# text to speech
def speak(text):
    if not text.strip():
        return
    # Re-initializing per call helps bypass Windows audio queue hangs
    temp_engine = pyttsx3.init()
    temp_engine.setProperty('rate', 150)
    temp_engine.say(text)
    temp_engine.runAndWait()

def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    
    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
        
        print("🔊 Speaking translation...")
        speak(translated_text)
        print("✅ Translation spoken out!")

if __name__ == "__main__":
    main()
