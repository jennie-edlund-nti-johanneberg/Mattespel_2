#Jennie
import turtle

def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y) 
    trtl.pd
    return

def kordinat_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du skriver in y-kordinaten och x-kordinaten till en punkt", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("x-kordinaten kan läsas genom att kolla vart punkten ligger på x-axeln.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540,100)
    trtl.write("x-axeln är den horisontella linjen", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 50)
    trtl.write("y-kordinaten hittas på samma sätt men du kollar på y-axeln. Den lodräta linjen.", font=('arial',15,'bold'), align='left')

    pos(trtl, 0, 0)
    trtl.pd()
    trtl.rt(0)
    trtl.fd(200)

    
    pos(trtl, -100, -100)
    trtl.pd()
    trtl.rt(-90)
    trtl.fd(200)

    #Pilen uppåt
    pos(trtl, -5, -5)
    trtl.write("^", font=("Verdana", 12, "bold"))

    #Pilen till höger
    pos(trtl, 100, -107) 
    trtl.write(">", font=("Verdana", 12, "bold"))

    #Skriver ut "x"
    pos(trtl, 100, -96)
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    #Skriver ut "y"
    pos(trtl, 10, -5)
    trtl.write("y",font=("Verdana", 12, "bold"))

    trtl.ht()
    #window.onscreenclick(trtl.clear())    #den aoutoklickar? vad är window? hur delectar jag hela canvas istället för window?
    #return
    #on klick (trtl.clear, return) #den ska i slutet rensa canvas och retunera(gå ur def så den landar tillbaka i main_2)

def kvadrant_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du skriver in vilken kvadrant en punkt befinner sig i", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Det finns fyra stycken kvadranter den första är längst uppe till höger.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540,100)
    trtl.write("Kolla bilden nedan:", font=('arial',15,'bold'), align='left')

    pos(trtl, 0, 0)
    trtl.pd()
    trtl.rt(0)
    trtl.fd(200)

    
    pos(trtl, -100, -100)
    trtl.pd()
    trtl.rt(-90)
    trtl.fd(200)

    #Pilen uppåt
    pos(trtl, -5, -5)
    trtl.write("^", font=("Verdana", 12, "bold"))

    #Pilen till höger
    pos(trtl, 100, -107) 
    trtl.write(">", font=("Verdana", 12, "bold"))

    #Skriver ut "x"
    pos(trtl, 100, -96)
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    #Skriver ut "y"
    pos(trtl, 10, -5)
    trtl.write("y",font=("Verdana", 12, "bold"))

    #Skriver ut "1"
    pos(trtl, 50, -50)
    trtl.write("1",font=("Verdana", 12, "bold"))

    #Skriver ut "2"
    pos(trtl, -50, -50)
    trtl.write("2",font=("Verdana", 12, "bold"))

    #Skriver ut "3"
    pos(trtl, -50, -150)
    trtl.write("3",font=("Verdana", 12, "bold"))

    #Skriver ut "4"
    pos(trtl, 50, -150)
    trtl.write("4",font=("Verdana", 12, "bold"))


    trtl.ht()
    window.exitonclick()

def givenGraf_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du skriver in vilken k-värde och m-värde funktionen", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("y = kx+m har som ritas ut", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("K-värdet kan räknas ut genom att ta ∆y/∆x = k. (Triangeln står för delta).", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Välj två punkter på funktionen. Ta sedan y-värdet på den ena punkten subtraherat med den andras.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 0)
    trtl.write("Dividera sedan värdet du får med (samma) förtsa punktens x-värdet subtraherat med den andras x-värde.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -50)
    trtl.write("Ett exemple med punkterna (2,2) och (4,8). Detta ger oss ∆y/∆x = (8-2)/(4-2) = 3. k = 3.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -100)
    trtl.write("(Tips är att ta punkten med större värden på x och y först).", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -150)
    trtl.write("M-värdet är y-värdet när funktionen går genom y-axeln eller när x = 0. Eftersom y=k*0+m => y = m", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -200)
    trtl.write("(Ibland kommer det inte synas när funktionen går genom x-axeln utan man får ränka på det)", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -250)
    trtl.write("Tycker du detta är svårt kan det vara bra att träna på kordinater mer!", font=('arial',15,'bold'), align='left')

    trtl.ht()
    window.exitonclick()

def expo_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du ska räkna ut vad y-värdet på en exponensialfunktion", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Exponensialfunktioner skrivs ut y = C*a^x och du kommer att få ut C-, a- och x-värdet.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("Här kan miniräknare vara ett bra hjälpmedel!", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Exemple kan vara y = 3*1^x där x = 2. Detta ger oss y = 3*1^2 = 3.", font=('arial',15,'bold'), align='left')

    trtl.ht()
    window.exitonclick()

def potensiell_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du ska räkna ut vad y-värdet på en potensfunktion", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Potensfunktioner skrivs ut y = C*x^a och du kommer att få ut C-, a- och x-värdet.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("Här kan miniräknare vara ett bra hjälpmedel!", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Exemple kan vara y = 3*x^4 där x = 2. Detta ger oss y = 3*2^4 = 48.", font=('arial',15,'bold'), align='left')

    trtl.ht()
    window.exitonclick()

def x_for_y_explain():

    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du ska räkna ut vad y-värdet på en räta linjens ekvation", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("Räta linjens ekvation skrivs ut y = kx+m och en sådan funktion kommer att ritas ut.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("Du kommer sedan att få ut ett x-värde och du får då mha grafen läsa av y-värdet där x-värdet är.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Ibland kan linjen vara utanför grafen och då är det upp till dig att räkna ut vad y-värdet är.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 0)
    trtl.write("Tex ser du att funktionen har ett k-värde på 3 och y = 4 när x = 5.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -50)
    trtl.write("Då kan vi räkna ut vad y-värdet är när x = 6 genom att ta 4+3 = 7. Svar: y = 7", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -100)
    trtl.write("Om detta är svårt kan det vara bra att kolla lite extra på räta linjens ekvation.", font=('arial',15,'bold'), align='left')

    trtl.ht()
    window.exitonclick()

def funktio_tabell_explain():

    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    pos(trtl, -540, 200)
    trtl.rt(90)
    trtl.write("Detta spelet går ut på att du skriver in vilken k-värde och m-värde funktionen", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 150)
    trtl.write("y = kx+m har genom en värdetabell", font=('arial',20,'bold'), align='left')

    pos(trtl, -540, 100)
    trtl.write("K-värdet kan räknas ut genom att ta ∆y/∆x = k. (Triangeln står för delta).", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 50)
    trtl.write("Välj två x- och y-världen (samma rad) från tabellen. Ta sedan y-värdet från ena raden subtraherat med den andras.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, 0)
    trtl.write("Dividera sedan värdet du får med x-värdet från (samma) första rad subtraherat med den andras x-värde.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -50)
    trtl.write("Ett exempel med värderna x1 = 2, y1 = 2 och x2 = 4, y2 = 8.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -100)
    trtl.write("Detta ger oss ∆y/∆x = (y2-y1)/(x2-x1) = (8-2)/(4-2) = 3. k = 3.", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -150)
    trtl.write("(Tips är att ta punkten med större värden på x och y först).", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -200)
    trtl.write("M-värdet är y-värdet när funktionen går genom y-axeln eller när x = 0. Eftersom y=k*0+m => y = m", font=('arial',15,'bold'), align='left')

    pos(trtl, -540, -250)
    trtl.write("Om inte tabellen visar vad y-värdet är när x = 0 får du räkna ut m-värdet själv. Detta mha k-värdet.", font=('arial',15,'bold'), align='left')

    trtl.ht()
    window.exitonclick()
