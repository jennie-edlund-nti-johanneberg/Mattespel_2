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
    screen = turtle.Screen()

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
    window.exitonclick()

def kvadrant_explain():
    window = turtle.Screen()
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)

    trtl = turtle.Turtle()
    screen = turtle.Screen()

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
    screen = turtle.Screen()

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

    trtl.ht()
    window.exitonclick()

givenGraf_explain()