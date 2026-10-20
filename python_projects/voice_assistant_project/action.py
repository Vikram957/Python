import text_to_speech
import speech_to_text
import datetime
import webbrowser
import random

def Action(data):
    if data is None or not str(data).strip():
        return "Please enter a message."

    user_data = str(data).strip().lower()
    # user_data = data.lower()

    if "what is your name" in user_data or "who are you" in user_data or "hu r u" in user_data or "what's your name" in user_data:
        text_to_speech.text_to_speech("I am your personal Python voice assistant")
        return "I am your personal Python voice assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hey, sir how can i help you")
        return "hey, sir how can i help you"

    elif "GoodMorning" in user_data or "good morning" in user_data:
        text_to_speech.text_to_speech("GoodMorning Sir")
        return "GoodMorning Sir"

    elif "whats time now" in user_data or "what time is it" in user_data or "time" in user_data:
        current_time = datetime.datetime.now()
        time = current_time.strftime("%I %M %p")
        text_to_speech.text_to_speech(f"Current Time is {time}")
        return time
    
    elif "whats date today" in user_data or "date" in user_data or "tell me todays date" in user_data:
            current_date = datetime.datetime.now()
            date = current_date.strftime("%d %B %Y")
            text_to_speech.text_to_speech(f"Today's date is {date}")
            return date

    elif "shutdown" in user_data or "shut down" in user_data or "close" in user_data:
        text_to_speech.text_to_speech("Ok Sir")
        return "Ok Sir"

    elif "play music" in user_data or "open spotify" in user_data or "song" in user_data or "music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("opening spotify for you")
        return "opening spotify for you"

    elif "youtube" in user_data or "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("opening youtube for you")
        return "opening youtube for you"


    elif "google" in user_data or "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("opening google for you")
        return "opening Google for you"

    elif "open gmail" in user_data:
        webbrowser.open("https://mail.google.com/")
        text_to_speech.text_to_speech("Opening Gmail")
        return "Opening Gmail"

    elif "open github" in user_data:
        webbrowser.open("https://github.com/Vikram957/Python")
        text_to_speech.text_to_speech("Opening GitHub")
        return "Opening GitHub"

    elif "who is the current prime minister of india" in user_data or "prime minister name" in user_data or "who is the prime minister of india" in user_data:
        text_to_speech.text_to_speech("Current prime Minister of India is Narendra Modi")
        return "Current prime Minister of India is Narendra Modi"

    elif "tell me a joke" in user_data or "make me laugh" in user_data:
        jokes = [
         "Why do programmers prefer dark mode? Because light attracts bugs!",
         "Why did the Python developer wear glasses? Because they couldn't C!",
         "Why do programmers love coffee? Because they need Java!"
    ]

        joke = random.choice(jokes)
        text_to_speech.text_to_speech(joke)
        return joke

    elif "what is python" in user_data:
        text_to_speech.text_to_speech("Python is a high-level, interpreted, general-purpose programming language known for its simple syntax, readability, and wide range of applications.")
        return "Python is a high-level, interpreted, general-purpose programming language known for its simple syntax, readability, and wide range of applications."

    elif "thankyou" in user_data or "thank you" in user_data:
        text_to_speech.text_to_speech("Welcome Sir")
        return "Welcome Sir"

    elif "chatgpt" in user_data or "open chatgpt" in user_data:
        webbrowser.open("https://chatgpt.com/")
        text_to_speech.text_to_speech("Opening Chatgpt")
        return "Opening Chatgpt"

    elif "how old are you" in user_data or "what is your age" in user_data:
        text_to_speech.text_to_speech("i am 1 month old")
        return "i am 1 month old"

    elif "who created you" in user_data:
        text_to_speech.text_to_speech("I was created by Vikram using Python.")
        return "I was created by Vikram using Python."

    elif "what can you do" in user_data or "tell me your functionalities" in user_data or "features" in user_data:
        text_to_speech.text_to_speech("I can open websites, tell the time and date, play music, and perform many other tasks.")
        return "I can open websites, tell the time and date, play music, and perform many other tasks."

    elif "motivate me" in user_data or "motivational quote" in user_data:
        text_to_speech.text_to_speech("Believe in yourself, work hard, and never stop learning.")
        return "Believe in yourself, work hard, and never stop learning."

    elif "i am bored" in user_data or "I'm bored" in user_data or "iam bored" in user_data:
        text_to_speech.text_to_speech("Let's do something fun. Would you like to listen to music?")
        return "Let's do something fun. Would you like to listen to music?"

    elif "good job" in user_data or "good work" in user_data or "good" in user_data:
        text_to_speech.text_to_speech("Thank you Sir, I am happy to help.")
        return "Thank you Sir, I am happy to help."

    elif "bye" in user_data or "goodbye" in user_data:
        text_to_speech.text_to_speech("Goodbye Sir, have a nice day.")
        return "Goodbye Sir, have a nice day."
  
    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"



    speech_to_text()