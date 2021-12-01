#Erik
import turtle
import random
import time

#Ger slumpade nummer mellan -5 och 5
def randomNumber():
    return (int(random.randint(-5, 5)))

def rand_nr():
    exclude=[0]
    randInt = random.randint(-4,4)
    return rand_nr() if randInt in exclude else randInt 

#Ger turtle position och färg
def pen(trtl, posx, posy, color):
    trtl.penup()
    trtl.color(color)
    trtl.setpos(posx, posy)
    trtl.pendown()

#Körs ifall användare fick rätt
def right(score):
    trtl = turtle.Turtle()
    trtl.color("black")
    style = ("Arial", 30, "italic")
    trtl.write("RÄTT!  Poäng:" + "{}".format(score), font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()
    return score

#Körs ifall användare fick fel
def wrong():
    trtl = turtle.Turtle()
    trtl.color("black")
    style = ("Arial", 30, "italic")
    trtl.write("FEL!", font=style, align="center")
    trtl.hideturtle()
    time.sleep(2)
    trtl.clear()

#ritar värdetabell
def värdetabell(trtl,scores ,x_1,x_2,x_3,y_1,y_2,y_3):
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
    trtl.setpos(-220,230-(25*1))
    trtl.pendown()
    trtl.write(f"{y_1}",font=("Verdana", 10, "bold"))
    
    trtl.pu()
    trtl.setpos(-220,230-(25*2))
    trtl.pendown()
    trtl.write(f"{y_2}",font=("Verdana", 10, "bold"))
    trtl.pu()
    
    trtl.setpos(-220,230-(25*3))
    trtl.pendown()
    trtl.write(f"{y_3}",font=("Verdana", 10, "bold"))
    trtl.pu()
    trtl.ht()

    kolla(trtl, x_1, x_2, y_1, y_2, scores)


#Kollar om användaren har samma svar som facit
def kolla(trtl, x_1, x_2, y_1, y_2, scores):

    #Själva skärmen läggs i variablen "sc"    
    sc = turtle.Screen()
    svark = 0
    #skapa facit
    facitk = int((y_2-y_1)/(x_2-x_1))#delar med 0 om de gissat 0 fixa de
    facitm = int(y_1-facitk*x_1)

    #användargiss
    while svark != None:
        try:
            svark = (sc.textinput("Vad är k-konstanten", "Ditt svar:"))
            if svark == "return":
                trtl.clear()
                return 
            svark = int(svark)
            
            svarm = (sc.textinput("Vad är m-konstanten", "Ditt svar:")) #obs här är det numera text
            if svarm == "return":
                trtl.clear()
                return 
            svarm = int(svarm)
        except (TypeError, OverflowError, ValueError):
            trtl_2 = turtle.Turtle()
            trtl_2.hideturtle()
            pen(trtl_2, 50, 100, "grey")
            trtl_2.write("Testa igen",font=("Verdana", 20, "bold"))
            time.sleep(0.5)
            trtl_2.clear()
            continue
        break

    
    #Skriver ut användarens svar
    pen(trtl, 50, 225, "black")
    if svarm < 0:
        trtl.write(f"Ditt svar: y = {svark}x{svarm}",font=("Verdana", 12, "bold"))
    elif svarm > 0:
        trtl.write(f"Ditt svar: y = {svark}x+{svarm}",font=("Verdana", 12, "bold"))
    else:
        trtl.write(f"Ditt svar: y = {svark}x",font=("Verdana", 12, "bold"))

    #Skriver ut rätt svar
    pen(trtl, 50, 207, "black")
    if facitm < 0:
        trtl.write(f"Rätt svar: y = {facitk}x{facitm}",font=("Verdana", 12, "bold"))
    elif facitm > 0:
        trtl.write(f"Rätt svar: y = {facitk}x+{facitm}",font=("Verdana", 12, "bold"))
    else:
        trtl.write(f"Rätt svar: y = {facitk}x",font=("Verdana", 12, "bold"))


    #Gömmer turtle och väntar 3 sekunder
    trtl.hideturtle()
    time.sleep(3)

#fixa hela undantagshanteringen

    #Kollar ifall användaren hade rätt
    if facitk == svark and facitm == svarm:
        scores["funktion_tabell"] += 1
        right(scores["funktion_tabell"])
    else:
        wrong()
        scores["funktion_tabell"]=0

    #Rensar turtle + skickar vidare ny score
    trtl.clear()
    game(scores)
    #sc.exitonclick() behöver ta bort


#Gör själva griden
def game(scores):
    #Skapar sköldpadda + hastigheten på den
    trtl = turtle.Turtle()
    trtl.speed(0)

    #x-linjerna
    for i in range(11):
        pen(trtl, -250, 250-(50*i), "lightgrey")
        trtl.fd(500)

    trtl.lt(90)

    #y-linjerna
    for i in range(11):
        pen(trtl, 250-(50*i), -250, "lightgrey")        
        trtl.fd(500)

    #Svart x-linje
    pen(trtl, 0, -250, "black")     
    trtl.fd(500)

    #Pilen till höger
    pen(trtl, 246, -8, "black") 
    trtl.write(">", font=("Verdana", 12, "bold"))

    #Svart y-linje
    pen(trtl, -250, 0, "black")
    trtl.rt(90)
    trtl.fd(500)

    #Pilen uppåt
    pen(trtl, -6, 240, "black")
    trtl.write("^", font=("Verdana", 12, "bold"))
     
    #Skriver ut "x"
    pen(trtl, 235, 0, "black")
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    #Skriver ut "y"
    pen(trtl, 5, 235, "black")
    trtl.write("y",font=("Verdana", 12, "bold"))
    
    #Skriver ut "1"
    pen(trtl, 5, 43, "black")
    trtl.write("1",font=("Verdana", 12, "bold"))

    #Skriver ut "1"
    pen(trtl, 46, 5, "black")
    trtl.write("1",font=("Verdana", 12, "bold"))
    
    #Skriver ut "y = kx+m"
    pen(trtl, -240, -235, "black")
    trtl.write("y = kx+m",font=("Verdana", 12, "bold"))

    #Skölpaddan riktas mot höger
    trtl.setheading(0)

    #ger massa saker massa värden
    k = randomNumber()
    m = randomNumber()
    #  
    #y = (k*x + m*50)
    #

    multiplyer=rand_nr()
    x_1 = randomNumber()
    x_2=x_1+multiplyer
    x_3=x_1+2*multiplyer

    y_1 = k*x_1+m
    y_2 = k*x_2+m
    y_3 = k*x_3+m
    #Plottar värdetabellen
    värdetabell(trtl,scores ,x_1,x_2,x_3,y_1,y_2,y_3)

    #Gömmer sköldpadda
    trtl.hideturtle()
    #turtle.done() bror bort med detta åsså

    #plotter(trtl, range(-250, 250), score)

