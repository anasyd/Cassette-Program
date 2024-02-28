import keyboard
import time
def normal():
    def thirty():
        print("Recording Started for 30 mins ")
        time.sleep(2100)
        keyboard.press_and_release("esc")
        time.sleep(30)
        keyboard.press_and_release("f2")
        time.sleep(1)
        keyboard.write(name)
        keyboard.press_and_release("enter")
        print("Saved!!")
    def sixty():
        print("Recording Started for 60 mins")
        time.sleep(3900)
        keyboard.press_and_release("esc")
        time.sleep(30)
        keyboard.press_and_release("f2")
        time.sleep(1)
        keyboard.write(name)
        keyboard.press_and_release("enter")
        print("Saved!!")
    def ninety():
        print("Recording Started for 90 mins")
        time.sleep(5760)
        keyboard.press_and_release("esc")
        time.sleep(30)
        keyboard.press_and_release("f2")
        time.sleep(1)
        keyboard.write(name)
        keyboard.press_and_release("enter")
        print("Saved!!")
    a=True
    while a==True:
        c=int(input("1.30 mins \n2.60 mins \n3.90 mins\n:"))
        name=input("Enter Name:")
        if c==1:
            thirty()
            print("BYE")
        elif c==2:
            sixty()
            print("BYE")
        elif c==3:
            ninety()
            print("BYE")
        else:
            a=False
            break

def  audacity():
    def thirty():
        print("Recording Started for 30 mins ")
        time.sleep(1920)
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
        
    def sixty():
        print("Recording Started for 60 mins")
        time.sleep(3900)
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
        
    def ninety():
        print("Recording Started for 90 mins")
        time.sleep(5760)
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
        
    a=True
    while a==True:
        c=int(input("1.30 mins \n2.60 mins \n3.90 mins\n:"))
        name=input("Enter Name:")
        if c==1:
            thirty()
            print("BYE")
        elif c==2:
            sixty()
            print("BYE")
        elif c==3:
            ninety()
            print("BYE")
        else:
            a=False

a=True
while a== True:
    c=int(input("1.Audacity \n2.Normal:"))
    if c==1:
        audacity()
        print("BYE")
    elif c==2:
        normal()
        print("BYE")
