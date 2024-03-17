import pyttsx3

def set_voice(engine, voice_name):
    voices = engine.getProperty('voices') # retrieve a list of available voices.
    for voice in voices:
        if voice_name in voice.name: # The break statement is used to exit the loop once the desired voice is found.
            engine.setProperty('voice', voice.id)
            break

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()



# trying to add this called main function :

    

    # Speak a test message
    
    
    
def main(speech: str | None):
    
    engine = pyttsx3.init()

    # Set the desired voice
    desired_voice = "Microsoft Zira Desktop - English (United States)"
    set_voice(engine, desired_voice)
    
    
    speak(speech, engine)


if __name__ == "__main__":
    main(speech="hey this is emmanuel")


