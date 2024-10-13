import pyaudio 
import os
import wave
import audioop
import speech_recognition as sr

class AudioListener:
    def __init__(self):
        # Assign the parameters values for audio capture
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second
        self.silence_threshold = 1500  # Adjust this threshold based on your environment
        self.silence_duration = 3  # 5 seconds of silence before stopping recording
        self.path = r"your_File_Path"  #path where temporary listener files are saved 

        # Create an interface to PortAudio
        self.p = pyaudio.PyAudio()

    def __call__(self):
        # Create an interface to PortAudio
        stream = self.p.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.fs,
            frames_per_buffer=self.chunk,
            input=True
        )

        frames = []  # Initialize array to store frames
        is_recording = True
        silence_timer = 0

        # Prompt user to say something
        print('Recording now - speak, and the recording will stop after ' + str(self.silence_duration) + ' seconds of silence.')

        while is_recording:
            data = stream.read(self.chunk)
            frames.append(data)

            # Perform speech detection
            audio_data = audioop.tomono(data, 2, 1, 0)
            if audioop.rms(audio_data, 2) < self.silence_threshold:
                # If the audio is below the silence threshold, start or reset the timer
                silence_timer += (self.chunk / self.fs)
            else:
                # If speech is detected, reset the timer
                silence_timer = 0

            # Check if the silence duration has been reached
            if silence_timer >= self.silence_duration:
                print(f"* Detected {self.silence_duration} seconds of silence. Stopping recording.")
                is_recording = False

        # Stop and close the input stream
        stream.stop_stream()
        stream.close()

        # Terminate the PortAudio interface
        self.p.terminate()

        print('Finished recording - saving file')

        # Save the recorded data as a WAV file
        filename = "outputLay.wav"
        wf = wave.open(os.path.join(self.path, filename), 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        # Convert the recorded wave file to text for use in openAI
        r = sr.Recognizer()
        audio_file_path = os.path.join(self.path, filename)
        with sr.AudioFile(audio_file_path) as source:
            audio = r.record(source)
            try:
                s = r.recognize_google(audio)
                return s  # Return the recognized text
            except Exception as e:
                print("Exception: " + str(e))
                return "none"  # Return None if there is an exception