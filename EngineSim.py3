from tkinter import *
import random
import time

Started = False
RPM = 0
Idle = False
Gear = N
Speed = int(0)
MaxRPM = 7500
MaxSpeed = 200
Redline = False

def Reset():
    Started = False
    RPM = 0
    Idle = False
    Gear = N
    Redline = False
    Speed = 0
    lbl2['text'] = RPM
    lbl8['text'] = Speed
    lbl4['text'] = Gear
    UpdateRPM()

def StartEngine():
    global Started
    global RPM
    global Idle
    Started = True
    Idle = True
    RPM = 900
    print("Engine running")
     
def UpdateRPM():
    global RPM
    global Gear
    global Redline
    
    if RPM >= MaxRPM:
        Redline = True
        print("Redline reached, throttle disengaged.")
        RPM = 7450
        lbl2['text'] = RPM
        window.after(1000,UpdateRPM)
    else:
        Redline = False
        
    if Started == True and Idle == True:
        OffsetRPM = random.randint(-10,10)
        lbl2['text'] = RPM + OffsetRPM
        window.after(1000,UpdateRPM)
    elif Started == True and Idle == False and RPM < 3000:
        OffsetRPM = random.randint(-10,10)
        lbl2['text'] = RPM + OffsetRPM
        window.after(1000,UpdateRPM)
    elif Started == True and Idle == False and RPM > 3000:
        OffsetRPM = random.randint(-10,10)
        if Gear < 5:
            Gear += 1
            RPM -= 1500
            lbl2['text'] = RPM + OffsetRPM
            print("Gear shifted up.")
            window.after(1000,UpdateRPM)
        else:
            lbl2['text'] = RPM + OffsetRPM            
            window.after(1000,UpdateRPM)
    elif Started == False:
        lbl2['text'] = RPM
        window.after(1000,UpdateRPM)
    
def StopEngine():
    global Started
    global RPM
    global Idle
    Started = False
    Idle = False
    RPM = 0
    print("Engine stopped")
    
 
def Accelerate():
    global RPM
    global Gear
    global Idle
    global Speed
    
    if Redline == True:
        "Redline reached, cannot accelerate further."
        time.sleep(3)
    else:
        RPM += 200
        Idle = False
        if Speed == 0:
            Speed = 1
            Gear = 1
        else:
            pass
        Speed += 5
        lbl8['text'] = int(Speed)
        lbl4['text'] = Gear
        
    
def Deccelerate():
    global RPM
    global Gear
    global Idle
    global Speed
    
    if RPM > 900 and RPM < 1400 and Gear > 1:
        RPM += 1000
        Speed = Speed*(0.6)
        Gear -= 1
        lbl4['text'] = Gear
        lbl8['text'] = int(Speed)
        window.after(2000,Deccelerate)
    elif RPM > 900:
        RPM -= 100
        Speed = Speed*(0.6)
        lbl8['text'] = int(Speed)
        window.after(2000,Deccelerate)
    else:
        Idle = True
        Speed = 0
        Gear = N
        lbl8['text'] = int(Speed)
        lbl4['text'] = Gear
        window.after(2000,Deccelerate)


window = Tk()
window.title("Engine Sim App")
window.geometry('350x200')
lbl1 = Label(window, text = "RPM:")
lbl1.grid(column=0,row=0)
lbl2 = Label(window, text = RPM)
lbl2.grid(column=1,row=0)
lbl3 = Label(window,text = "Gear:")
lbl3.grid(column=0,row=1)
lbl4 = Label(window,text = Gear)
lbl4.grid(column=1,row=1)
lbl7 = Label(window,text = "Speed:")
lbl7.grid(column=0,row=3)
lbl8 = Label(window,text = int(Speed))
lbl8.grid(column=1,row=3)

btn1 = Button(window,text="Start Engine",command=StartEngine)
btn1.grid(column=2,row=0)

btn2 = Button(window,text="Stop Engine",command=StopEngine)
btn2.grid(column=3,row=0)

btn3 = Button(window,text="Accelerate",command=Accelerate)
btn3.grid(column=2,row=1)

btn4 = Button(window,text="Deccelerate",command=Deccelerate)
btn4.grid(column=3,row=1)

btn5 = Button(window,text="Reset",command=Reset)
btn5.grid(column=3,row=3)



UpdateRPM()
Deccelerate()
window.mainloop()