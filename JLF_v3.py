#----class files---------
from JLFtext_to_speech import TextToSpeechCaller
from JLFaudio_listener import AudioListener
from JLFchat_completions import ChatCompletions
#-----------------------------
from openai import OpenAI
import numpy as np
import time
import subprocess
import random
#----action files--------
import weather_action
import maps_action
import youtube_action
import chrome_action
from gpt_action import gpt_action
#-------------------
from responses import initialRes

chatApiKey = "your_API_Key"
chatAssistant = "You are a helpful assistant who is somewhat sarcastic."

client = OpenAI(api_key=chatApiKey)

speak = TextToSpeechCaller()

# IDLE State
state = '(idle)'
while state == '(idle)':
    state = '(idle)'
    print(state)

    # Create an instance of the class
    listen = AudioListener()
    Userinput = listen()
    
    Userinput = Userinput.lower()

    #Res 1 state
    if Userinput in ['hey jarvis', 'jarvis you there', 'jarvis are you there']:
        state = '(Res 1)'
        print(state)

        #initialize/create the 2D chat array starting with the system directive about the assitant
        arr = np.array([["system", chatAssistant]])  #system content

        #set flag to indicate we are in the loop state
        loopState = 'yes'

        random_case_number = random.randint(1, 4)

        # Call the initial response function with the random case number
        iRes = initialRes(random_case_number)

        #print("you called?")
        speak(iRes)
        time.sleep(3)

        #listening state
        while loopState == 'yes':
            state = '(listening)'
            print(state)


            listen = AudioListener()
            Userinput2 = listen()
            Userinput2 = Userinput2.lower()

            #Back to idle state
            if Userinput2 in ['thank you', 'nevermind']:
                state = '(idle)'

                #set flag to indicate we are no longer in the loop state
                loopState = 'no'

                break
            #~~~~~~~~~~~~~~~~~~~~~~~
            #Weather state
            elif Userinput2 == 'what is the weather':
                state = '(weatherAPI)'
                weather_action.get_weather()

            #Maps state
            elif Userinput2 == 'i am looking to travel':
                state = '(Res 3)'
                maps_action.travel_action()

            #Open Youtube
            elif Userinput2 == 'open youtube':
                youtube_action.youtube_action()

            #Launch Chrome
            elif Userinput2 == 'open chrome':
                chrome_action.chrome_actions('open')

            #Close Chrome
            elif Userinput2 == 'close chrome':
                chrome_action.chrome_actions('close')

            #GPT state
            elif Userinput2 != 'none':
                #--------callable file but doesnt remember conversation----
                #gpt_action(arr, client, speak, Userinput2)
                #--------------------------------------------------------
                state = '(GPT)'
                print(state)

                # 1st user question added to the 2D chat array 
                arr = np.append(arr, [["user", Userinput2]], axis=0)

                # Call the internal class for an OpenAI chat response
                chat_instance = ChatCompletions(arr, client)
                r1 = chat_instance.get_response()

                # Add answer to the 2D chat array so the context of the conversation is maintained
                arr = np.append(arr, [["assistant", str(r1)]], axis=0)

                speak(str(r1))
                time.sleep(12)
