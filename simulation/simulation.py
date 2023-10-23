import turtle
import time
import main
import threading
import ray

window = turtle.Screen()
window.title("Traffic simulation")
window.bgcolor("black")


class StopLight:
    def __init__(self, x, y, i):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(x - 30, y + 60)
        self.pen.pendown()
        self.pen.color("yellow")
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.color = ""
        self.redLight = turtle.Turtle()
        self.orangeLight = turtle.Turtle()
        self.greenLight = turtle.Turtle()
        self.redLight.speed(0)
        self.orangeLight.speed(0)
        self.greenLight.speed(0)
        self.redLight.shape("circle")
        self.orangeLight.shape("circle")
        self.greenLight.shape("circle")
        self.redLight.penup()
        self.orangeLight.penup()
        self.greenLight.penup()
        self.redLight.goto(x, y + 40)
        self.orangeLight.goto(x, y)
        self.greenLight.goto(x, y - 40)
        self.redLight.color("gray")
        self.orangeLight.color("gray")
        self.greenLight.color("gray")

        self.number = turtle.Turtle()
        self.number.hideturtle()
        self.number.penup()
        self.number.goto(x, y + 80)
        self.number.pendown()
        self.number.color("white")
        self.number.write(i)

    def ChangeColor(self, color):
        self.redLight.color("gray")
        self.orangeLight.color("gray")
        self.greenLight.color("gray")
        if color == "red":
            self.redLight.color("red")
            self.color = "red"
        elif color == "orange":
            self.orangeLight.color("orange")
            self.color = "orange"
        elif color == "green":
            self.greenLight.color("green")
            self.color = "green"

    def setTimmer(self):
        if self.color == "red":
            self.ChangeColor("green")
            window.ontimer(self.setTimmer, 8000)
        elif self.color == "orange":
            self.ChangeColor("red")
            window.ontimer(self.setTimmer, 1000)
        elif self.color == "green":
            self.ChangeColor("orange")
            window.ontimer(self.setTimmer, 6000)


signal1 = StopLight(0, 0, 1)
signal1.ChangeColor("green")

signal2 = StopLight(-100, 0, 2)
signal2.ChangeColor("red")

signal3 = StopLight(100, 0, 3)
signal3.ChangeColor("red")

signal4 = StopLight(200, 0, 4)
signal4.ChangeColor("red")

currentSignals = [signal1.color, signal2.color, signal3.color, signal4.color]


def signal_loop():
    interupt = False
    if currentSignals.index("green") == 0:
        signal1.ChangeColor(currentSignals[0])
        time.sleep(8)
        signal1.ChangeColor("orange")
        time.sleep(2)
        signal1.ChangeColor("red")
        signal2.ChangeColor("green")
        currentSignals[0] = "red"
        currentSignals[1] = "green"
        interupt = False
    # print("0")
    elif currentSignals.index("green") == 1:
        signal2.ChangeColor(currentSignals[1])
        time.sleep(8)
        if currentSignals.index("green") != 1:
            #signal_loop()
            signal2.ChangeColor("orange")
            time.sleep(2)
            signal2.ChangeColor("red")
        else:
            signal2.ChangeColor("orange")
            time.sleep(2)
            signal2.ChangeColor("red")
            signal3.ChangeColor("green")
            currentSignals[1] = "red"
            currentSignals[2] = "green"
            # print("1")
            #signal_loop()
            interupt = False
    elif currentSignals.index("green") == 2:
        signal3.ChangeColor(currentSignals[2])
        time.sleep(8)
        if currentSignals.index("green") != 2:
            #signal_loop()
            signal3.ChangeColor("orange")
            time.sleep(2)
            signal3.ChangeColor("red")
        else:
            signal3.ChangeColor("orange")
            time.sleep(2)
            signal3.ChangeColor("red")
            signal4.ChangeColor("green")
            currentSignals[2] = "red"
            currentSignals[3] = "green"
            #signal_loop()
            interupt = False
    elif currentSignals.index("green") == 3:
        signal4.ChangeColor(currentSignals[3])
        time.sleep(8)
        if currentSignals.index("green") != 3:
            #signal_loop()
            interupt = False
            signal4.ChangeColor("orange")
            time.sleep(2)
            signal4.ChangeColor("red")
        else:
            signal4.ChangeColor("orange")
            time.sleep(2)
            signal4.ChangeColor("red")
            signal1.ChangeColor("green")
            currentSignals[3] = "red"
            currentSignals[0] = "green"
            #signal_loop()
            interupt = False
    loop(0,interupt)

def loop(singnalNum,interupt):
        currentGreen = currentSignals.index("green")
        if interupt == True:
            for num in range(0,currentSignals.__len__()):
                if num == singnalNum:
                    currentSignals[num] = "green"
                else:
                    currentSignals[num] = "red"
            print("interupt signal",currentSignals)
            print(currentGreen)
            if currentGreen==0:
                signal1.ChangeColor("orange")
                time.sleep(2)
                signal1.ChangeColor("red")
            elif currentGreen==1:
                signal2.ChangeColor("orange")
                time.sleep(2)
                signal2.ChangeColor("red")
            elif currentGreen==2:
                signal3.ChangeColor("orange")
                time.sleep(2)
                signal3.ChangeColor("red")
            elif currentGreen==3:
                signal4.ChangeColor("orange")
                time.sleep(2)
                signal4.ChangeColor("red")
            signal_loop()
            time.sleep(1)
        else:
            signal_loop()
        #loop(0,False)

while True:
    loop(3,main.imageProcessing())
    print("signal interuption called")

#window.mainloop()