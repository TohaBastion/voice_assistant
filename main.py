import time

import speech_recognition as sr
from output import speak


def main():
    recognizer = sr.Recognizer()
    speak(text="Привіт, я твій голосовий помічник! Чим можу допомогти?")

    while True:
        with sr.Microphone() as source:
            print("готовий")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language='uk-UA')
                if text.lower() == "привіт":
                    print(f'Ви сказали: {text}')
                    speak('Вітаю, мій володар!')
                    time.sleep(2)
                else:
                    speak("Я не розчула команду.")
                    time.sleep(2)
            except sr.UnknownValueError:
                print('Не вдалося розпізнати звук')
            except sr.RequestError:
                print('request error')
            except sr.WaitTimeoutError:
                print("timeout")


if __name__ == '__main__':
    main()
