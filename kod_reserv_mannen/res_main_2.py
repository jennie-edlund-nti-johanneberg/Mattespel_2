import turtle
import time
def minigames(user_choise):
    print(user_choise)

def flytt(trtl, length):
    trtl.pu()
    trtl.fd(length)
    trtl.pd

def game_hub():
    trtl = turtle.Turtle()
    trtl.speed(0)
    trtl.ht()
    trtl.pu()
    trtl.setpos(-315, 250) 
    trtl.pd
    trtl.rt(90)
    flytt(trtl,30)
    trtl.write("Välkommen till mattespelet!", font=("Arial", 35, "italic"), align="left")
    flytt(trtl,40)
    trtl.write("Det finn en hel del roliga mattespel att välja mellan!", font=("Arial", 20, "italic"), align="left")
    flytt(trtl,30)
    minispel=["bestämning av x och y-kordinat av en punkt","bestämning av kvadrant en punkt befinner sig i","räta linjens ekvation (Y=kx+m)","värdetabelövning för räta linjer","att ge funktionsvärde på spesifika x värden i y=kx+m","potensialfunktioner","exponnsialfunktioner"]
    for n in (minispel):
        trtl.write("För "+ n +" skriv in siffran "+str(minispel.index(n)), font=("Arial", 12, "italic"), align="left")
        flytt(trtl,20)

    flytt(trtl,40)
    trtl.write("När du känner dig färdig med ett minispel kan du", font=("Arial", 20, "italic"), align="left")
    flytt(trtl,40)
    trtl.write("återvända hit genom att svara XXX på någon fråga", font=("Arial", 20, "italic"), align="left")
    flytt(trtl,150)
    trtl.write("Lycka till!", font=("Arial", 80, "italic"), align="left")

    time.sleep(10)
    sc = turtle.Screen()
    user_input=int(sc.numinput("vart vill du 0-10","Ditt val:"))
    minigames(user_input)
    turtle.done()

game_hub()


#import funktio_tabell
#import givenGraf
#import kordinater
#import kvadrant
#import tabellGraf
