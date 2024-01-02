from tkinter import *
from googletrans import Translator
import pyttsx3
import speech_recognition as sr


root=Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = screenwidth
y = screenheight
root.geometry("640x720")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        speak("wait for few minutes")
        print("wait for few minutes")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please")
    return query
if __name__ == "__main__":
    while True:
        query = takecommand().lower()
def trans(text,target_language="hi"):
    translator=Translator()
    translated_text=translator.translate(text,dest=target_language)
    return translated_text.text
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    if printButton:
        tran = trans(inp, target_language='en')
    if speakbut:
        tran=trans(query,target_language='en')
    lbl.config(text=tran)

inputtxt = Text(root,height=5,width=20)
inputtxt.pack()
# Button Creation
printButton = Button(root,text="Print",command=printInput)
printButton.pack()
speakbut=Button(root,text="speak",command=takecommand)
speakbut.pack()
diut=Button(root, text="Quit", command=root.destroy)
diut.pack()
lbl = Label(root, text = "")
lbl.pack()
root.mainloop()