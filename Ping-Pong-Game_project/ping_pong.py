import turtle                                        #* // LMODUL DYAL RSM (TURTLE) //

#! XAXA :
WIND = turtle.Screen()                               #* // XLA9A TA3 L3BA //
WIND.title("🎾 PING PONG BY 🅱🅼 🅽🅰🅿🅾🅻🅸 🎾")      #* // 3ONWAN XAXA //
WIND.bgcolor("black")                                #* // LAWN XAXA //
WIND.setup(width=800, height=600)                    #* // TOL O 3ARD XAXA //
WIND.tracer(0)                                       #* // KAY7BES L UPDATE BAX NHLU CONTROL //

#! DADRAB 1 :
MADRAB1 = turtle.Turtle()                            #* // NJIBO OBJET JDID MN TURTLE //
MADRAB1.speed(0)                                     #* // A9SA SOR3A MMKINA [0] //
MADRAB1.shape("square")                              #* // XAKL AL MADRAB [MORABA3] //
MADRAB1.color("Magenta")                             #* // LAWN LMOJASSAM //
MADRAB1.shapesize(stretch_wid=5, stretch_len=1)      #* // ITALAT LMOJASAM //
MADRAB1.penup()                                      #* // KAYMSE7 L5OTOT //
MADRAB1.goto(-350, 0)                                #* // I7DATIYAT LMJASSAM //

#! DADRAB 2 :
MADRAB2 = turtle.Turtle()                            #* // OBJET JDID //
MADRAB2.speed(0)                                     #* // A9SA SOR3A //
MADRAB2.shape("square")                              #* // MORABA3 //
MADRAB2.color("Cyan")                                #* // LAWN //
MADRAB2.shapesize(stretch_wid=5, stretch_len=1)      #* // TOL MADRAB //
MADRAB2.penup()                                      #* // BLA ATHAR //
MADRAB2.goto(350, 0)                                 #* // I9AMAT LMADRAB F LIMIN //

#! BALLE :
BALLE = turtle.Turtle()                              #* // OBJET LKORA //
BALLE.speed(0)                                       #* // SOR3A MAX //
BALLE.shape("circle")                                #* // DAYERA //
BALLE.color("gray")                                  #* // LAWN //
BALLE.shapesize(stretch_wid=1, stretch_len=1)        #* // 9IYASS LKORA //
BALLE.penup()                                        #* // BLA ATHAR //
BALLE.goto(0, 0)                                     #* // LMERKAZ //
BALLE.dx = 0.2                                       #* // SOR3A F X //
BALLE.dy = 0.2                                       #* // SOR3A F Y //

#! SCORE :
SCOR1 = 0                                            #* // SCORE PLAYER 1 //
SCOR2 = 0                                            #* // SCORE PLAYER 2 //
SCOR = turtle.Turtle()                               #* // OBJET L AFFICHAGE //
SCOR.speed(0)                                        #* // SOR3A //
SCOR.color("WHITE")                                  #* // LAWN //
SCOR.penup()                                         #* // BLA ATHAR //
SCOR.hideturtle()                                    #* // MANKHLIHCH YBAN //
SCOR.goto(0, 260)                                    #* // POSITION F LFOQ //
SCOR.write("PLAYER 1 : 0  /  PLAYER 2 : 0", align="center", font=("Courier", 24, "normal"))  #* // LKTABA LFOQ //

#TODO L7RAKA DYAL MADARIB :
def MADRAB1_up():                                    #* // FONCTION TLE3 MADRAB1 //
    y = MADRAB1.ycor()                               #* // NJIB L I7DATIYAT F Y //
    if y < 250:                                      #* // MA YTLA3CH 3LA L7IT //
        y += 30                                      #* // N7ARK B +30 //
        MADRAB1.sety(y)                              #* // NRJ3O LFO9 //

def MADRAB1_down():                                  #* // FONCTION TNA9S MADRAB1 //
    y = MADRAB1.ycor()                               #* // NJIB L I7DATIYAT F Y //
    if y > -250:                                     #* // MA YHBATCH 3LA L7IT //
        y -= 30                                      #* // N7ARK -30 //
        MADRAB1.sety(y)                              #* // NRJ3O LTA7T // 

def MADRAB2_up():                                    #* // FONCTION TLE3 MADRAB2 //
    y = MADRAB2.ycor()                               #* // NJIB L I7DATIYAT F Y //
    if y < 250:                                      #* // 7AD MAX F LFO9 //
        y += 30                                      #* // N7ARK B +30 //
        MADRAB2.sety(y)                              #* // NRJ3O LFO9 //

def MADRAB2_down():                                  #* // FONCTION TNZL MADRAB2 //
    y = MADRAB2.ycor()                               #* // NJIB L I7DATIYAT F Y //
    if y > -250:                                     #* // 7AD MIN F LTA7T //
        y -= 30                                      #* // N7ARK -30 //
        MADRAB2.sety(y)                              #* // NRJ3O LTA7T // 

#TODO INPUTS DYAL CLAVIER :
WIND.listen()                                        #* // NSTANAW AWAMIR MN LCLAVIER //
WIND.onkeypress(MADRAB1_up, "Up")                    #* // CLIK 'UP' = TLE3 MADRAB1 //
WIND.onkeypress(MADRAB1_down, "Down")                #* // CLIK 'DOWN' = TNZL MADRAB1 //
WIND.onkeypress(MADRAB2_up, "q")                     #* // CLIK 'Q' = TLE3 MADRAB2 //
WIND.onkeypress(MADRAB2_down, "a")                   #* // CLIK 'A' = TNZL MADRAB2 //

#TODO LA7ALA9A :
while True:                                          #* // LOOP DIMA TDOOR //
    WIND.update()                                    #* // KANDIRO UPDATE L XAXA //

    #TODO HRAKAT LKORA :
    BALLE.setx(BALLE.xcor() + BALLE.dx)              #* // T7AROK F X //
    BALLE.sety(BALLE.ycor() + BALLE.dy)              #* // T7AROK F Y //

    #? BORDER CHECK (LFOK W LTAHT) :
    if BALLE.ycor() > 290:                           #* // ILA TL3AT FOQ //
        BALLE.sety(290)                              #* // NRJ3OHA LFOQ L7AD //
        BALLE.dy *= -1                               #* // N9ELBO ITIJAH //

    if BALLE.ycor() < -290:                          #* // ILA HBBAT THT //
        BALLE.sety(-290)                             #* // NRJ3OHA LTA7T L7AD //
        BALLE.dy *= -1                               #* // N9ELBO ITIJAH //

    #? BORDER CHECK F JM3 JHAT :
    if BALLE.xcor() > 390:                           #* // ILA FATT L YMIN //
        BALLE.goto(0, 0)                             #* // RJA3NA LKORA L LMERKAZ //
        BALLE.dx *= -1                               #* // BDALNA L ITIJAHA F X //
        SCOR1 += 1                                   #* // ZD SCORE L PLAYER 1 //
        SCOR.clear()                                 #* // MSE7NA SCORE QDIM //
        SCOR.write("PLAYER 1 : {}  /  PLAYER 2 : {}".format(SCOR1, SCOR2), align="center", font=("Courier", 24, "normal"))  #* // KTEBNA SCORE JDID //

    if BALLE.xcor() < -390:                          #* // ILA FATT L YSR //
        BALLE.goto(0, 0)
        BALLE.dx *= -1
        SCOR2 += 1                                   #* // ZD SCORE L PLAYER 2 //
        SCOR.clear()
        SCOR.write("PLAYER 1 : {}  /  PLAYER 2 : {}".format(SCOR1, SCOR2), align="center", font=("Courier", 24, "normal"))

    #? TASADOM MA3A MADRAB2 :                            
    if BALLE.xcor() >= 340 and BALLE.xcor() <= 350 and BALLE.ycor() < MADRAB2.ycor() + 60 and BALLE.ycor() > MADRAB2.ycor() - 60:
        BALLE.setx(340)                              #* // RJA3NA LKORA L LHED DYAL MADRAB 2 //
        BALLE.dx *= -1                               #* // BDALNA ITIJAHA F X //

    #? TASADOM MA3A MADRAB1 :                           
    if BALLE.xcor() <= -340 and BALLE.xcor() >= -350 and BALLE.ycor() < MADRAB1.ycor() + 60 and BALLE.ycor() > MADRAB1.ycor() - 60:
        BALLE.setx(-340)                             #* // RJA3NA LKORA L LHED DYAL MADRAB 1 //
        BALLE.dx *= -1                               #* // BDALNA ITIJAHA F X //
