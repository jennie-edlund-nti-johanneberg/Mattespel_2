import turtle
import time
scores = {"koordinater":0,"kvadrant":0, "givengraf":0, "potensiell":0, "x_for_y":0, "funktion_tabell":0}

def minigames(user_choise):
    global scores
    if user_choise==0:
        #tell text
        import kordinater
        kordinater.padda(scores)
    elif user_choise==1:
        #tell text
        import kvadrant
        kvadrant.game(scores)
    elif user_choise==2:
        #tell text
        import givenGraf
        givenGraf.grid(scores)
    elif user_choise==3:
        #tell text
        import funktio_tabell
        funktio_tabell.game(scores)
        print(user_choise)
    elif user_choise==4:
        #tell text
        import x_for_y
        x_for_y.grid(scores)
        print(user_choise)
    elif user_choise==5:
        #tell text
        #run program
        print(user_choise)
    elif user_choise==6:
        #tell text
        #run program
        print(user_choise)
    else:
        #run program
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
    trtl.write("återvända hit genom att svara return på någon fråga", font=("Arial", 20, "italic"), align="left")
    flytt(trtl,150)
    trtl.write("Lycka till!", font=("Arial", 80, "italic"), align="left")

    time.sleep(1)
    sc = turtle.Screen()
    user_input=int(sc.numinput("vart vill du 0-10","Ditt val:"))
    while user_input<0 or user_input>10:
        user_input=int(sc.numinput("vart vill du 0-10","Ditt val:"))
    #lägg in undantagshanterin input=infinity
    turtle.clearscreen()
    
    minigames(user_input)
    turtle.clear()
    game_hub()

game_hub()


#import funktio_tabell
#import givenGraf
#import kordinater
#import kvadrant
#import tabellGraf
