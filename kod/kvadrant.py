#Erik
import math
import time
import random
import turtle
def rand_cord():
    return int(random.randint(-5,5))





def cord_system():
    trtl = turtle.Turtle()

    #trtl.ht()

    trtl.speed(10)
    trtl.color("lightgrey")
    
    #vågräta(horrisontella) linjer
    for i in range(11):
        trtl.pu()
        trtl.setx(-250)
        trtl.sety(250-(50*i))
        trtl.pd() 
        trtl.fd(500)

    #left trun (90deg)
    trtl.lt(90)

    #Lodräta(vertikal) linjer
    for i in range(11):
        trtl.pu()
        trtl.sety(-250)
        trtl.setx(250-(50*i))
        trtl.pd() 
        trtl.fd(500)

    trtl.color("black")

    #rita y-axel
    trtl.pu()
    trtl.setx(0)
    trtl.sety(-250)
    trtl.pd() 
    trtl.fd(500)

    #rita x-axel
    trtl.pu()
    trtl.setx(-250)
    trtl.sety(0)
    trtl.rt(90)
    trtl.pd() 
    trtl.fd(500)

    x_cord = rand_cord()
    y_cord = rand_cord()

    #flö trtl till cord
    trtl.pu()
    trtl.setx(50*x_cord)
    trtl.sety(50*y_cord)

    #rita upp prick 
    trtl.color("red","red")
    trtl.begin_fill()
    trtl.circle(7)
    trtl.end_fill()
    
    #Fråga vilken kvadrant cord är i
    guess()


def guess():
    return input("Vilken kvadrant ligger punkten i?")
