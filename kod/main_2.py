import turtle

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
    trtl.write("För x skriv in siffran n", font=("Arial", 13, "italic"), align="left")
    flytt(trtl,25)
    trtl.write("För x skriv in siffran n", font=("Arial", 13, "italic"), align="left")
    flytt(trtl,25)
    trtl.write("För x skriv in siffran n", font=("Arial", 13, "italic"), align="left")
    flytt(trtl,25)
    trtl.write("För x skriv in siffran n", font=("Arial", 13, "italic"), align="left")
    flytt(trtl,25)
    trtl.write("För x skriv in siffran n", font=("Arial", 13, "italic"), align="left")
    flytt(trtl,25)
    trtl.write("För x skriv in siffran n", font=("Arial", 13, "italic"), align="left")
    flytt(trtl,60)
    trtl.write("När du känner dig färdig med ett minispel kan du", font=("Arial", 20, "italic"), align="left")
    flytt(trtl,40)
    trtl.write("återvända hit genom att svara XXX på någon fråga", font=("Arial", 20, "italic"), align="left")
    flytt(trtl,150)
    trtl.write("Lycka till!", font=("Arial", 80, "italic"), align="left")


    #skriv välkomen till spel och hur man går vidare till minispel
    #tar input t.ex nummer 1-8 vad de vill göra för minispel
    #if sats på alla spel som följer
    #if user_input ==1:
    #   #förklara hur 1 är
    #   kör filen för 1;a minispel
    # elif user_input==2:
    #   förklara hur 2 är
    #   kör filen för 2:a minispel
    #så vidare så vidare

    turtle.done()

game_hub()


#import funktio_tabell
#import givenGraf
#import kordinater
#import kvadrant
#import tabellGraf
