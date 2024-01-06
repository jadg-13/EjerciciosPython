import speech_recognition as sr
import subprocess
import pyautogui
import datetime as dt

recognizer = sr.Recognizer()
process = None
greeting = "Hola, bienvenido a esta prueba de voz\n"

def execute_command(command):
    global process
    if "abrir notepad" in command:
        process = subprocess.Popen(["notepad.exe"])
    elif "cerrar notepad" in command:
        process.terminate()
    elif "saludar" in command:
        pyautogui.write(greeting)


    
def listen():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="es-ES")  
            print("Has dicho: " + command)
            execute_command(command)

        except sr.UnknownValueError:
            print("No te he entendido")
        except sr.RequestError as e:
            print("Error al llamar a Google Speech Recognition service; {0}".format(e))
        
while True:
    listen()
