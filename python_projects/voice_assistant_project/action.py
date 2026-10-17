import text_to_speech
import speech_to_text
import datetime
import webbrowser

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data or "who are you" in user_data or "hu r u" in user_data:
        text_to_speech.text_to_speech("My name is virtual Assistant")
        return "My name is virtual Assistant"

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

    elif "play music" in user_data or "open spotify" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("opening spotify for you")
        return "opening spotify for you"

    elif "youtube" in user_data or "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("opening youtube for you")
        return "opening youtube for you"


    elif "Google" in user_data or "open Google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("opening google for you")
        return "opening Google for you"


    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"