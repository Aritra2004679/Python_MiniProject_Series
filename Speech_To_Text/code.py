import speech_recognition as sr

AUDIO_FILE = "sample_audio.wav"

# Initialize recognizer
r = sr.Recognizer()

# Read audio file
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# Convert speech to text
try:
    print("Audio file contains:\n")

    text = r.recognize_google(audio, language="hi-IN")

    print(text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError:
    print("Couldn't get results from Google Speech Recognition")