import keyboard
import time

def thirty():
    print("Recording Started for 30 mins ")
    time.sleep(1920)
    
def sixty():
    print("Recording Started for 60 mins")
    time.sleep(3900)

    
def ninety():
    print("Recording Started for 90 mins")
    time.sleep(5760)


def save_default_recorder(name):

    keyboard.press_and_release("esc")
    time.sleep(30)
    keyboard.press_and_release("f2")
    time.sleep(1)
    keyboard.write(name)
    keyboard.press_and_release("enter")
    print("Saved!!")

def  save_audacity(name):
    keyboard.press_and_release("space")
    time.sleep(3)
    keyboard.press_and_release("alt")
    keyboard.press_and_release("f")
    keyboard.press_and_release("e")
    keyboard.press_and_release("3")
    time.sleep(1)
    keyboard.write(name)
    keyboard.press_and_release("enter")
    time.sleep(1)
    keyboard.press_and_release("enter")
    print("Saved!!")
        

programRunning = True
while programRunning == True:

    softwareList = [save_audacity, save_default_recorder]
    softwareSelected = save_audacity

    softwareChoice = int(input("1.Audacity \n2.Normal\n0.Exit\n:"))

    if softwareChoice == 1:
        softwareSelected = save_audacity

    elif softwareChoice == 2:
        softwareSelected = save_default_recorder

    elif softwareChoice == 0:
        print("BYE")
        programRunning = False
        break


    minsChoice=int(input("1.30 mins \n2.60 mins \n3.90 mins\n0.Exit\n:"))

    if minsChoice == 0:
        programRunning = False
        break

    name=input("Enter Name:")
    if minsChoice==1:
        thirty()
        softwareSelected(name)

    elif minsChoice==2:
        sixty()
        softwareSelected(name)

    elif minsChoice==3:
        ninety()
        softwareSelected(name)
