import pyttsx3
import os
pyttsx3.speak("Welcome to my Softwares")
while True:
    print("------------------------------------------------")
    print("Open any softwares as your wish: ",end='')
    p = input()
    if((("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome browser" in p) or ("browser" in p))):
        pyttsx3.speak("Opening the chrome browser")
        os.system("chrome")

    elif((("run" in p) or ("execute" in p) or ("open" in p) or ("play" in p)) and (" media player" in p)):
        pyttsx3.speak("Opening the windows media player")
        os.system("wmplayer")

    elif((("run" in p) or ("execute" in p) or ("open" in p) or ("play" in p)) and ("video player" in p)):
        pyttsx3.speak("Opening the vlc player")
        os.system("vlc")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("notepad" in p) or ("editor" in p))):
        pyttsx3.speak("Opening the notepad IDE")
        os.system("notepad")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("ardiuno" in p) or ("editor" in p))):
        pyttsx3.speak("Opening the ardiuno IDE")
        os.system("ardiuno")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("codeblocks" in p) or ("editor" in p))):
        pyttsx3.speak("Opening the CodeBlocks IDE")
        os.system("codeblocks")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("DEV C++" in p) or ("editor" in p) or ("IDE" in p))):
        pyttsx3.speak("Opening the Dev C++ IDE")
        os.system("devcpp")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("notepad++" in p) or ("editor" in p) or ("IDE" in p))):
        pyttsx3.speak("Opening the notepad++ IDE")
        os.system("notepad++")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("oracle" in p) or ("virtualbox" in p) or ("IDE" in p))):
        pyttsx3.speak("Opening the Oracle VirtualBox")
        os.system("virtualbox")

    elif((("run" in p) or ("execute" in p) or ("open" in p)) and (("text" in p) or ("sublime text" in p) or ("editor" in p) or ("IDE" in p))):
        pyttsx3.speak("Opening the Sublime Text Editor")
        os.system("sublime_text")

    elif("exit" in p) or ("quit" in p):
        break

    else:
        pyttsx.speak("Programs are not avalilable")
        print("---------------------------------------")
        print("Does not support")
        print("---------------------------------------")



    
