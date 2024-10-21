import os
from gtts import gTTS
import pygame


def speak(text):
    # Ініціалізуємо звуковий модуль pygame кожного разу перед відтворенням
    pygame.mixer.init()

    tts = gTTS(text=text, lang='uk', slow=False)
    filename = 'outputTTSs.mp3'
    tts.save(filename)

    # Завантажуємо і відтворюємо аудіо через pygame
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Очікуємо завершення відтворення
    while pygame.mixer.music.get_busy():
        pass

    # Зупиняємо відтворення і закриваємо модуль перед видаленням файлу
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Видаляємо файл після відтворення
    os.remove(filename)
