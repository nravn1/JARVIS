from openai import OpenAI
from pathlib import Path
from pygame import mixer
from datetime import datetime

chatApiKey = "your_API_Key"
client = OpenAI(api_key = chatApiKey)

class TextToSpeechCaller:
    def __call__(self, text):
        # Time stamp
        current_time = datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d-%H-%M-%S")

        # Create speech file path
        speech_file_path = Path(__file__).parent / f"speech{timestamp_str}.mp3"


        # Generate speech using OpenAI API
        response = client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=text
        )
        response.stream_to_file(speech_file_path)

        # Initialize mixer and play the speech
        mixer.init()
        mixer.music.load(str(speech_file_path))
        mixer.music.play()
