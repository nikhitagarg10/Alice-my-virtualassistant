import PySimpleGUI as gui
import pywhatkit
import time
import cv2
import speech_recognition as sr
from playsound import playsound
import threading
from gtts import gTTS

gui.theme("DarkBlack1")

def text_screen_next(name):
    layout = [  [gui.Text("Hello {}. How may I help you ?".format(name))],
                [gui.InputText(), gui.Button("ASK"), gui.Button("PLAY")],[gui.Button("GO BACK"), gui.Button("CANCEL")]]
    window = gui.Window("Virtual Assistent", layout)

    name = str(name)
    txt = "Hello "+name+" How may I help you ?"

    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("4.mp3")
    playsound("4.mp3", block=False)

    while True:
            event, values = window.read()
            if event==gui.WIN_CLOSED or event=="CANCEL":
                break
            elif (event=="GO BACK"):
                window.close()
                first_screen()
            else:
                curr = time.ctime()
                tlist = list(curr.split(" "))

                if (values[0] == "take screenshot"):
                    pywhatkit.take_screenshot("myscreenshot")
                elif(event == "PLAY"):
                    if(values):
                        pywhatkit.playonyt(values[0])
                    else:
                        pass
                elif(values[0] == "what time it is"):
                    ans = tlist[3]
                    gui.popup_ok(ans, grab_anywhere=True)
                elif(values[0] == "what day it is"):
                    ans = tlist[0] + " " + tlist[1] + " " +  tlist[2] + " " +  tlist[4]
                    gui.popup_ok(ans, grab_anywhere=True)
                elif(values[0] == "what year it is"):
                    ans = tlist[4]
                    gui.popup_ok(ans, grab_anywhere=True)
                elif(values[0] == "open camera"):
                    cap = cv2.VideoCapture(0)
                    i = 0
                    while True:
                        ret, frame = cap.read()
                        cv2.imshow('Input', frame)
                        c = cv2.waitKey(1)
                        if c == 13:
                            cv2.imshow(str(i),frame)
                            flag = DOu()
                            if(flag):
                                cv2.imwrite("{}.png".format(flag), frame)
                            i = i + 1
                        elif c == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                else:
                   if(values):
                        pywhatkit.search(values[0])               
    window.close()

def text_screen():

    layout = [  [gui.Text("Hello I am Alice. What is your name"),],
                [gui.InputText(), gui.Button("DONE")],[gui.Button("GO BACK"), gui.Button("CANCEL")]]
    window = gui.Window("Virtual Assistent", layout)

    txt = "Hello I am Alice. What is your name"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("3.mp3")
    playsound("3.mp3", block=False)

    while True:
            event, values = window.read()
            if event==gui.WIN_CLOSED or event=="CANCEL":
                break
            elif (event=="GO BACK"):
                first_screen()
            elif (event=="DONE"):
                name = values[0]
                window.close()
                text_screen_next(name)
    window.close()

def speech_screen():
    layout = [  [gui.Text("Hello I am Alice. What is your name ?"),],
                [gui.Button("SPEAK")],[gui.Button("GO BACK"), gui.Button("CANCEL")]]
    
    
    window = gui.Window("Virtual Assistent", layout)

    txt = "Hello I am Alice. What is your name"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("3.mp3")
    playsound("3.mp3", block=False)

    while True:
            event, values = window.read()
            if event==gui.WIN_CLOSED or event=="CANCEL":
                break
            elif (event=="GO BACK"):
                first_screen()
            elif (event=="SPEAK"):
                r = sr.Recognizer()
                mic = sr.Microphone(device_index=1)
                try:
                    with mic as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        res = r.recognize_google(audio)
                        window.close()
                        speech_screen_next(res)
                        
                except:
                    print("OOps!, sorry I did not get that")
    window.close()
    
def speech_screen_next(res):
    layout = [  [gui.Text("Hello {}. How may I help you".format(res))],
                [gui.Button("SPEAK"),gui.Button("GO BACK"), gui.Button("CANCEL")]]
    window = gui.Window("Virtual Assistent", layout)

    txt = "Hello"+res+"How may I help you"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("4.mp3")
    playsound("4.mp3", block=False)

    while True:
            event, values = window.read()
            if event==gui.WIN_CLOSED or event=="CANCEL":
                break
            elif (event=="GO BACK"):
                window.close()
                first_screen()
            elif (event == "SPEAK"):
                curr = time.ctime()
                tlist = list(curr.split(" "))
                r = sr.Recognizer()
                mic = sr.Microphone(device_index=1)
                try:
                    with mic as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        ans = r.recognize_google(audio)
                        if (ans == "screenshot"):
                            pywhatkit.take_screenshot("myscreenshot")
                        elif(ans == "what time it is"):
                            ans = tlist[3]
                            gui.popup_ok(ans, grab_anywhere=True)
                        elif(ans == "what day it is"):
                            answer = tlist[0] + " " + tlist[1] + " " +  tlist[2] + " " +  tlist[4]
                            gui.popup_ok(answer, grab_anywhere=True)
                        elif(ans == "what year it is"):
                            answer = tlist[4]
                            gui.popup_ok(answer, grab_anywhere=True)
                        elif(ans == "open camera"):
                            cap = cv2.VideoCapture(0)
                            i = 0
                            while True:
                                ret, frame = cap.read()
                                cv2.imshow('Input', frame)
                                c = cv2.waitKey(1)
                                if c == 13:
                                    cv2.imshow(str(i),frame)
                                    flag = DOu()
                                    if(flag):
                                        cv2.imwrite("{}.png".format(flag), frame)
                                    i = i + 1
                                elif c == 27:
                                    break
                            cap.release()
                            cv2.destroyAllWindows()
                        else:
                            ans1 = str(ans)
                            if(ans1.find("play") == -1):
                                pywhatkit.search(ans1) 
                            else:
                                pywhatkit.playonyt(ans1)

                except:
                    print("Oops!, sorry I did not get that")
                    
    window.close()

def first_screen():

    layout = [  [gui.Text("Hey I am Alice. How would you like me to help you?"),],
                [gui.Button("SPEECH"),gui.Button("TEXT"),gui.Button("CANCEL")]]

    window = gui.Window("Virtual Assistent", layout)

    txt = "Hey I am Alice. How would you like me to help you"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("1.mp3")
    playsound("1.mp3", block=False)
    t = threading.Timer(3.5, play)
    t.start()
    while True:
            event, values = window.read()
            if event==gui.WIN_CLOSED or event=="CANCEL":
                break
            elif (event=="SPEECH"):
                window.close()
                speech_screen()
            elif (event=="TEXT"):
                window.close()
                text_screen()
    window.close()

def play():
    txt = "Press speech to enable voice options. Press text to enable chat options"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("2.mp3")
    playsound("2.mp3", block=False)

def naming():
    layout = [[gui.Text("enter the name of the picture file")],
                      [gui.InputText(), gui.Button("DONE")]]
    window = gui.Window("Virtual Assistent", layout)
    '''txt = "enter the name of the picture file"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("5.mp3")
    playsound("5.mp3", block=False)'''
    while True:
        event, values = window.read()
        if (values[0] == False):
            pass
        else:
            window.close()
            return values[0]

def DOu():
    layout = [[gui.Text("do you want to save this file?")],
              [gui.Button("YES"), gui.Button("NO")]]
    window = gui.Window("Virtual Assistent", layout)
    txt = "do you want to save this file?"
    myobj = gTTS(text=txt, tld='com.au', lang="en", slow=False)
    myobj.save("5.mp3")
    playsound("5.mp3", block=False)
    while True:
        event, values = window.read()
        if event=="NO":
            flag = False
            window.close()
            return flag 
        elif event=="YES":
            flag = True
            window.close()
            return naming() 

first_screen()