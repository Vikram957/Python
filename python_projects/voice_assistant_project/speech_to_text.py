import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        voice_data = ""
        voice_data = r.recognize_google(audio)
        print(voice_data)
        return voice_data
    
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""

    except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return ""

# speech_to_text()


    