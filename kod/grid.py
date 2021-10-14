import turtle

def grid():
    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.color("lightgrey")

    for i in range(11):
        trtl.pu()
        trtl.setx(-250)
        trtl.sety(250-(50*i))
        trtl.pd() 
        trtl.fd(500)

    trtl.lt(90)

    for i in range(11):
        trtl.pu()
        trtl.setx(250-(50*i))
        trtl.sety(-250)
        trtl.pd() 
        trtl.fd(500)

    trtl.pu()
    trtl.setx(0)
    trtl.sety(-250)
    trtl.color("black")
    trtl.pd() 
    trtl.fd(500)

    # set position again
    trtl.penup()
    trtl.setpos(246,-8)
    trtl.pendown()

    trtl.write(">", font=("Verdana", 12, "bold"))

    trtl.pu()
    trtl.setx(-250)
    trtl.sety(0)
    trtl.rt(90)
    trtl.pd() 
    trtl.fd(500)

    trtl.penup()
    trtl.setpos(-6,240)
    trtl.pendown()

    trtl.write("^", font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(235,0)
    trtl.pendown()
     
    # write x
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(5,235)
    trtl.pendown()
     
    # write y
    trtl.write("y",font=("Verdana", 12, "bold"))
    
    trtl.hideturtle()

    turtle.done()


grid()