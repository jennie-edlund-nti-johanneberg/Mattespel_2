#gör till test 2
lista=["wef","wed","sdf","kjf"]
for i in lista:
    print("i listan är " + i + " på plats "+str(lista.index(i)))


import turtle
def värdetabell(trtl ,x_1,x_2,x_3,y_1,y_2,y_3):
    trtl.pu()
    trtl.setx(-250)
    trtl.sety(250)
    trtl.pd()
    trtl.color("black")
    trtl.sety(150)
    trtl.setx(-200)
    trtl.sety(250)
    trtl.setx(-250)
    for i in range (4):
        trtl.setx(-250)
        trtl.sety(250-(50*i/2))
        trtl.pd()
        trtl.fd(50)
        trtl.pu()
    trtl.setx(-225)
    trtl.sety(250)
    trtl.lt(270)
    trtl.pd()
    trtl.fd(100)
    trtl.pu()

    trtl.setpos(-240,230)
    trtl.pendown()
    trtl.write("x",font=("Verdana", 10, "bold"))
    trtl.pu()
        
    trtl.setpos(-215,230)
    trtl.pendown()
    trtl.write("y",font=("Verdana", 10, "bold"))

    #x-values
    
    trtl.pu()
    trtl.setpos(-240,230-(25*1))
    trtl.pendown()
    trtl.write(f"{x_1}",font=("Verdana", 10, "bold"))
    
    trtl.pu()
    trtl.setpos(-240,230-(25*2))
    trtl.pendown()
    trtl.write(f"{x_2}",font=("Verdana", 10, "bold"))
    trtl.pu()
    
    trtl.setpos(-240,230-(25*3))
    trtl.pendown()
    trtl.write(f"{x_3}",font=("Verdana", 10, "bold"))
    trtl.pu()

    #y-values
       
    trtl.pu()
    trtl.setpos(-215,230-(25*1))
    trtl.pendown()
    trtl.write(f"{y_1}",font=("Verdana", 10, "bold"))
    
    trtl.pu()
    trtl.setpos(-215,230-(25*2))
    trtl.pendown()
    trtl.write(f"{y_2}",font=("Verdana", 10, "bold"))
    trtl.pu()
    
    trtl.setpos(-215,230-(25*3))
    trtl.pendown()
    trtl.write(f"{y_3}",font=("Verdana", 10, "bold"))
    trtl.pu()

    


    







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
    # set position again
    trtl.penup()
    trtl.setpos(5,43)
    trtl.pendown()
    # write 1
    trtl.write("1",font=("Verdana", 12, "bold"))
    # set position again
    trtl.penup()
    trtl.setpos(46,5)
    trtl.pendown()
    # write 1
    trtl.write("1",font=("Verdana", 12, "bold"))
    trtl.hideturtle()

    värdetabell(trtl,1,2,3,6,7,8)
    turtle.done()
grid()
