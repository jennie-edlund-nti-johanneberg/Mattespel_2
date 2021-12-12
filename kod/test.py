#Jennie (testar kod här)
import turtle

# def flytt(trtl, length):
#     trtl.pu()
#     trtl.fd(length)
#     trtl.pd

def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y)
    trtl.pd
    return

def test():
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(231, 228, 237)
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)
    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    trtl.pu()

    pos(trtl, -320, 230) 
    trtl.write("Välkommen till ett mattespel mannen!", font=("Time New Roman", 22, "bold"), align="left")

    pos(trtl, -300, 170) 

    minispel=["Bestämning av x och y-kordinat av en punkt","Bestämning av kvadrant en punkt befinner sig i","Räta linjens ekvation (Y=kx+m)","Värdetabelövning för räta linjer","Att ge funktionsvärde på spesifika x värden i y=kx+m","Potensialfunktioner","Exponnsialfunktioner"]
    temp = 0

    for n in (minispel):

        # trtl.write("För "+ n +" skriv in siffran "+str(minispel.index(n)), font=("Verdana", 12, "normal"), align="left")

        trtl.write(str(minispel.index(n)) + " - " + n +"skriv in siffran ", font=("Time New Roman", 15, "normal"), align="left")


        temp += 1
        x_kord = (170 - temp*30)
        pos(trtl, -300, x_kord)

    pos(trtl, -320, -90)
    trtl.write("Du tar dig tillbaka genom att skriva return!!!!", font=("Time New Roman", 15, "bold"), align="left")

    pos(trtl, -320, -120)
    trtl.write("Lycka till!", font=("Time New Roman", 15, "normal"), align="left")

    trtl.ht()
    window.exitonclick()

test()

    # trtl = turtle.Turtle()

    # trtl.speed(0)
    # trtl.ht()
    # trtl.pu()
    # trtl.setpos(-315, 250) 
    # trtl.pd
    # trtl.rt(90)
    # flytt(trtl,30)
    # trtl.write("Välkommen till mattespelet!", font=("Arial", 35, "italic"), align="left")
    # flytt(trtl,40)
    # trtl.write("Det finn en hel del roliga mattespel att välja mellan!", font=("Arial", 20, "italic"), align="left")
    # flytt(trtl,30)
    # minispel=["bestämning av x och y-kordinat av en punkt","bestämning av kvadrant en punkt befinner sig i","räta linjens ekvation (Y=kx+m)","värdetabelövning för räta linjer","att ge funktionsvärde på spesifika x värden i y=kx+m","potensialfunktioner","exponnsialfunktioner"]
    # for n in (minispel):
    #     trtl.write("För "+ n +" skriv in siffran "+str(minispel.index(n)), font=("Arial", 12, "italic"), align="left")
    #     flytt(trtl,20)

    # flytt(trtl,40)
    # trtl.write("När du känner dig färdig med ett minispel kan du", font=("Arial", 20, "italic"), align="left")
    # flytt(trtl,40)
    # trtl.write("återvända hit genom att svara return på någon fråga", font=("Arial", 20, "italic"), align="left")
    # flytt(trtl,150)
    # trtl.write("Lycka till!", font=("Arial", 80, "italic"), align="left")