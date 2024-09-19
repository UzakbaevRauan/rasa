# import requests
# import speech_recognition as sr
# import subprocess
# from gtts import gTTS

# # Определение функции для воспроизведения текста
# def speak(text):
#     if not text:
#         print("No text to speak.")
#         return
#     tts = gTTS(text=text, lang='en')
#     tts.save("response.mp3")
#     print('Saved response as response.mp3')
#     # Воспроизведение сохранённого файла
#     subprocess.call(['vlc', '--play-and-exit', '--no-video', "response.mp3"])

# # Отправка начального сообщения боту и получение ответа
# def get_bot_response(message):
#     try:
#         response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})
#         response.raise_for_status()  # Проверка на ошибки HTTP
#         return response.json()
#     except requests.RequestException as e:
#         print(f"Error sending request to bot: {e}")
#         return []

# # Начальное сообщение боту
# bot_message = "Hello"

# # Отправка начального сообщения и получение ответа
# responses = get_bot_response(bot_message)
# if responses:
#     bot_message = responses[0].get('text', '')
#     print(f"Bot says: {bot_message}")
#     speak(bot_message)
# else:
#     print("No response from the bot")

# # Начало интерактивного цикла
# while bot_message.lower() not in ["bye", "thanks"]:
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak Anything:")
#         audio = r.listen(source)
#         try:
#             user_message = r.recognize_google(audio)
#             print(f"You said: {user_message}")

#         except sr.UnknownValueError:
#             print("Sorry, could not recognize your voice")
#             continue
#         except sr.RequestError:
#             print("Sorry, there was an issue with the request")
#             continue
    
#     if not user_message:
#         continue
    
#     print("Sending message now...")
    
#     # Отправка сообщения пользователя боту
#     responses = get_bot_response(user_message)
#     if responses:
#         bot_message = responses[0].get('text', '')
#         print(f"Bot says: {bot_message}")
        
#         # Воспроизведение сообщения бота, если оно не пустое
#         if bot_message:
#             speak(bot_message)
#     else:
#         print("No response from the bot")
import os
import requests
import json
import pygame
from gtts import gTTS

# Настройка для Rasa сервера
RASA_SERVER = "http://localhost:5005/webhooks/rest/webhook"

def send_message_to_bot(message):
    """Отправляет сообщение в Rasa бот и получает ответ."""
    payload = {
        "message": message
    }
    response = requests.post(RASA_SERVER, json=payload)
    return response.json()

def speak(text):
    """Воспроизводит текст как аудио с использованием gTTS и pygame."""
    if not text:
        print("No text to speak.")
        return
    
    # Удаление старого файла, если существует
    if os.path.exists("response.mp3"):
        os.remove("response.mp3")
    
    # Сохранение текста как аудио
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    print('Saved response as response.mp3')
    
    # Инициализация pygame и воспроизведение аудио
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():  # Ждем, пока музыка не закончится
        pygame.time.Clock().tick(10)

def main():
    while True:
        user_input = input("Speak Anything: ")
        print(f"You said: {user_input}")

        # Отправка сообщения боту
        bot_response = send_message_to_bot(user_input)
        if bot_response:
            # Получение ответа бота и вывод его на экран
            bot_message = bot_response[0]['text'] if 'text' in bot_response[0] else 'No response from bot'
            print(f"Bot says: {bot_message}")

            # Воспроизведение ответа бота
            speak(bot_message)
        else:
            print("No response from bot.")

if __name__ == "__main__":
    main()
