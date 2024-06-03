# IMPORTING VARIOUS LIBRARIES
import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

# INITIALISE SPEECH RECOGNIZER
listener = sr.Recognizer()
# INITIALISE PYWHATKIT
speaker = pyttsx3.init()

# RATE OF SPEAKER 
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 140)

# SPEAKER VOICE 
voices = speaker.getProperty('voices')
if len(voices) > 1:
    speaker.setProperty('voice', voices[1].id)
else:
    speaker.setProperty('voice', voices[0].id)

# SPEAK FUNCTION
def speak(text):
    speaker.say(text)
    speaker.runAndWait()

# INTRO GREETINGS
speak('Hey, I am Luna, how can I assist you?')

# COMMAND FUNCTION
def feed_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "luna" in command:
                command = command.replace("luna ", '')
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
    except:
        print("Check your microphone.")
    return command

while True:
    user_command = feed_command()
    # STOP COMMAND TO CLOSE THE ASSISTANT
    if "stop" in user_command or "hey luna stop" in user_command:
        print('Let me know if you need any help!')
        speak("Let me know if you need any help!")
        break
    # ASKING TIME 
    elif "what's the current time" in user_command or 'time' in user_command:
        current_time = dt.datetime.now().strftime("%I:%M %p")
        print(f"It's {current_time}")
        speak(f"It's {current_time}")
    # ASKING DATE
    elif "what's the date today" in user_command or "today's date" in user_command:
        todays_date = dt.datetime.now().strftime("%Y-%m-%d")
        print(f"Today's date = {todays_date}")
        speak(f"Today's date is {todays_date}")
    # PLAYING ON YT
    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print(f'Playing {user_command}')
        speak(f'Playing {user_command}')
        pk.playonyt(user_command)
        break
    # SEARCH ON GOOGLE
    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for ', '')
        user_command = user_command.replace('google ', '')
        print(f'Searching for {user_command}')
        pk.search(user_command)
        break
    # GET INFORMATION FROM WIKIPEDIA
    elif 'who is' in user_command or 'what is' in user_command or 'tell me about' in user_command:
        user_command = user_command.replace('who is ', '')
        user_command = user_command.replace('what is ', '')
        user_command = user_command.replace('tell me about ', '')
        info = wiki.summary(user_command, 2)
        print(info)
        speak(info)
        break
    # ASKING ABOUT "LUNA"
    elif 'who are you' in user_command:
        speak('I am Luna, your virtual assistant.')
        break
    else:
        speak("Please say it loudly, I didn't understand you.")
