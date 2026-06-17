'''from gtts import gTTS
import pygame

text = input("Jo bolna hai likh: ")

tts = gTTS(text=text, lang='en')   # hindi ke liye lang='hi'
tts.save("voice.mp3")

pygame.mixer.init()
pygame.mixer.music.load("voice.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
print("Sab chal raha hai 😎")'''
from gtts import gTTS
import pygame

text = input("Jo bolna hai likho: ")

tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")

pygame.mixer.init()
pygame.mixer.music.load("voice.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue