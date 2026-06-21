import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Boliye ab...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Aapne bola:", text)

except Exception as e:
    print(type(e).__name__)
    print(e)