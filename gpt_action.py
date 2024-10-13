
import numpy as np
from JLFchat_completions import ChatCompletions
from JLFtext_to_speech import TextToSpeechCaller
import time

def gpt_action(arr, client, speak, Userinput2):
    state = '(GPT)'
    print(state)

    # 1st user question added to the 2D chat array 
    arr = np.append(arr, [["user", Userinput2]], axis=0)

    # Call the internal class for an OpenAI chat response
    chat_instance = ChatCompletions(arr, client)
    r1 = chat_instance.get_response()

    # Add the answer to the 2D chat array so the context of the conversation is maintained
    arr = np.append(arr, [["assistant", str(r1)]], axis=0)

    speak(str(r1))
    time.sleep(12)
