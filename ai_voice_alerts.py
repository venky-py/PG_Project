from gtts import gTTS
import os
import pygame

def play_alert(message):
    tts = gTTS(message, lang="en")
    tts.save("alert.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("alert.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

play_alert("Fire detected! Notify rescue team immediately.")
