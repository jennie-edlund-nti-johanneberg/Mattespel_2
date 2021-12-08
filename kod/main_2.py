import turtle
import time
#import explain
scores = {"koordinater":0,"kvadrant":0, "givengraf":0, "potensiell":0, "x_for_y":0, "funktion_tabell":0, "expo": 0}

def minigames(user_choise):
    global scores
    if user_choise==0:
        #tell text
        #explain.kordinat_explain()
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
    elif user_choise==4:
        #tell text
        import x_for_y
        x_for_y.grid(scores)
    elif user_choise==5:
        #tell text
        import potensiell
        potensiell.grid(scores)
    elif user_choise==6:
        #tell text
        import expo
        expo.grid(scores)
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

    #ta in user input oc se till att de är en intiger mellan 0 0ch (6+1) hehe annars få dem att skriva in igen
    sc = turtle.Screen()
    user_input=0
    while user_input != None:
        try:
            user_input = int(sc.numinput("vart vill du 0-7","Ditt val:"))
            if not 0 <= user_input <= 7:
                raise ValueError
        except (TypeError, OverflowError, ValueError):
            time.sleep(1)
            continue
        break

    turtle.clearscreen()
    
    minigames(user_input)
    turtle.clear()
    game_hub()

game_hub()

#undantagshantering så man inte kan trycka cancle

#import funktio_tabell
#import givenGraf
#import kordinater
#import kvadrant
#import tabellGraf
