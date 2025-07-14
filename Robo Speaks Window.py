import win32com.client

print("Hello, Pycharm. Let's Code")
speaker = win32com.client.Dispatch("SAPI.SpVoice")
name = input("Enter your name : ")
greeting = f"Hey, let's start {name}"
print(greeting)
speaker.Speak(greeting)
speaker.Speak('Enter what you want me to speak')

while True:
    text = input("Enter what you want to speak: ")
    print(text)
    speaker.Speak(text)
