from pynput import keyboard

tercih=None
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def on_press(key):

    global tercih
    if key==keyboard.Key.left:

        tercih=True
        return False
    elif key==keyboard.Key.right:
        tercih=False
        return False

    elif key==keyboard.Key.esc:
        tercih="quit"
        return False




def getanswer(whattoprint):
    #cls()
    print(whattoprint)
    with keyboard.Listener(
            on_press=on_press,
            on_release=None) as listener:
        listener.join()
        return tercih

if __name__ =="__main__":
    print(getanswer())


