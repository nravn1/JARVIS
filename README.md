# JARVIS
This is a program that allows you to talk to an assistant and receive accurate information. The information is powered by ChatGPT. Go to the "master" branch for the code.
You will need your OpenAI API key in the "JLF_v3" and "JLFtext_to_speech" files as well as your file path of choice in the "JLFaudio_listener" file.
The following libraries need to be installed: numpy openai pygame pyaudio 
The program works by flowing through differnt states. It will start idle until you trigger it by saying "hey Jarvis" or "Jarvis you there?". Once triggered, you can then ask it any number of questions or to do a limited number of tasks I have in to fill. If you ask an info question, it takes your question and sends it off to ChatGPT and runs whatever engine you have it on (default is 3.5 so if you want current events change to newer model) before receiving the JSON and sending it off again to the text-to-speech API by OpenAI. If you dont like the voice, you are able to change it (default is fable). It then speaks the answer back to you and waits for a delay before listening to your next question. The default delay is set to 12s to avoid it from listening to itself. You can then tell it "thank you" or "nevermind" to send it back into its idle starting state until you say "hey jarvis" again. 
