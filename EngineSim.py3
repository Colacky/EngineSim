from tkinter import *
import random

Started = False
RPM = 0
Idle = False
Gear = N
Speed = 0
MaxRPM = 7500
MaxSpeed = 200
Power = 0

def StartEngine():
    global Started
    global RPM
    global Idle
    Started = True
    Idle = True
    RPM = 900
    print("Engine running")

def ChangeGears():
    global RPM
    global Speed
    global Gear
    ShiftUp = False
    
    while RPM > 3000:
        ShiftUp = True
        print("Ready to shift gears.")
        window.after(100,ChangeGears)
    
    while ShiftUp == True:
        Gear += 1
        lbl4['text'] = Gear
        RPM -= 1500
        lbl2['text'] = RPM
        print("Gear shifted up")
        ShiftUp = False
        window.after(100,ChangeGears)    
    
def UpdateRPM():
    if Started == True and Idle == True:
        OffsetRPM = random.randint(-10,10)
        lbl2['text'] = RPM + OffsetRPM
        window.after(500,UpdateRPM)
    elif Started == True and Idle == False:
        OffsetRPM = random.randint(-10,10)
        lbl2['text'] = RPM + OffsetRPM
        window.after(500,UpdateRPM)
    elif Started == False:
        lbl2['text'] = RPM
        window.after(500,UpdateRPM)
    
def StopEngine():
    global Started
    global RPM
    global Idle
    Started = False
    Idle = False
    RPM = 0
    print("Engine stopped")
    
def CalcPower():
    global Power
    global RPM
    Power = int(RPM/54)
    lbl6['text'] = Power
    window.after(100,CalcPower)
 
def Accelerate():
    global RPM
    global Gear
    global Idle
    global Speed
    RPM += 100
    Idle = False
    if Speed == 0:
        Speed = 1
        Gear = 1
    else:
        pass
    Speed = Speed*1.1
    lbl8['text'] = Speed
    lbl4['text'] = Gear
    print("Increased speed.")
    
def Deccelerate():
    global RPM
    global Gear
    global Idle
    global Speed
    if RPM > 900:
        RPM -= 100
        Speed = Speed/(0.6)
        lbl8['text'] = Speed
        print("Decreased speed.")
        window.after(1500,Deccelerate)
    else:
        Idle = True
        Speed = 0
        Gear = N
        lbl8['text'] = Speed
        lbl4['text'] = Gear
        print("Stopped.")
        window.after(1500,Deccelerate)


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
lbl5 = Label(window,text = "Power:")
lbl5.grid(column=0,row=2)
lbl6 = Label(window,text = Power)
lbl6.grid(column=1,row=2)
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

ChangeGears()
CalcPower()
UpdateRPM()
Deccelerate()
window.mainloop()