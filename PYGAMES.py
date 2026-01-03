#---imports---# 
import turtle as t
import time as ti
import random as r

#---global.variables---#
score = 0
high_score = 0
target = 10

#t.Snap()
def snap(val):
    return round(val / 20) * 20

#---antgame---#
def antgame():
    #---setup---#

    #t.Screen()
    scr = t.Screen()
    scr.title("Ant Game")
    scr.bgcolor("#FACA72")
    scr.setup(600, 600)
    scr.tracer(0)

    #t.ScoreDef()
    global score, high_score

    #t.head()
    h = t.Turtle()
    h.shape('turtle')
    h.color("#ff2600")
    h.penup()
    h.speed(0)
    h.showturtle()
    h.direction = 'stop'
    h.setheading(90)

    #t.foods()
    f = t.Turtle()
    f.shape('circle')
    f.penup()
    f.color("#F3D6D6")
    f.speed(0)
    f.showturtle()
    f.direction = 'stop'
    f.goto(0, 60)

    d = t.Turtle()
    d.shape('circle')
    d.penup()
    d.color("#EDAB48")
    d.speed(0)
    d.showturtle()
    d.direction = 'stop'
    d.goto(0, -60)

    #t.Bomb()
    b = t.Turtle()
    b.shape('circle')
    b.penup()
    b.color("#052304")
    b.speed(0)
    b.showturtle()
    b.direction = 'stop'
    b.goto(60, -60)

    
    #t.pen()
    p = t.Turtle()
    p.color("#171717")
    p.hideturtle()
    p.penup()
    p.direction = 'stop'
    p.goto(0, 267)
    p.write(f"Score: {score} | Highscore: {high_score}", align= "center", font= ("Monospace", 20, 'bold'))

    #-----Functions--------#

    #t.Move()
    def move():
        if h.direction == "up":
            y = h.ycor()
            h.sety(y+20)
        
        if h.direction == "down":
            y = h.ycor()
            h.sety(y-20)

        if h.direction == "left":
            x = h.xcor()
            h.setx(x-20)

        if h.direction == "right":
            x = h.xcor()
            h.setx(x+20)

    #t.Controls()
    def go_up():
        if h.direction != "down":
            h.direction = "up"
            h.setheading(90)
    def go_down():
        if h.direction != "up":
            h.direction = "down"
            h.setheading(270)
    def go_left():
        if h.direction != "right":
            h.direction = "left"
            h.setheading(180)
    def go_right():
        if h.direction != "left":
            h.direction = "right"
            h.setheading(0)

    #t.GameOver()
    def gameover():

        #t.Endgame()
        h.hideturtle()
        f.hideturtle()
        d.hideturtle()
        b.hideturtle()

        ti.sleep(0.5)
        p.clear()
        p.goto(0, 0)
        p.write("Game Over!", align= "center", font= ("Monospace", 20, 'bold'))
        scr.update()
        p.clear()
        ti.sleep(1)

        #t.RestartAnimation()
        p.clear()
        p.write("Restarting", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.3)
        
        p.clear()
        p.write("Restarting.", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.3)
        
        p.clear()
        p.write("Restarting..", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.3)
        
        p.clear()
        p.write("Restarting...", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.67)
        
        #t.NewScoring()
        global score, high_score
        p.clear()
        p.goto(0, 267)

        if score > high_score:
            high_score = score
        score = 0
        p.write(f"Score: {score} | Highscore: {high_score}", align="center", font=("Monospace", 20, 'bold'))
        scr.update()

        #t.Respawn()
        h.goto(0, 0)
        h.direction = 'stop'
        h.color("#ff0000")
        h.setheading(90)

        f.goto(0, 60)
        f.direction = 'stop'

        d.goto(0, -60)
        d.direction = 'stop'

        b.goto(60, -60)
        b.direction = 'stop'
        b.color("#052304")

        h.showturtle()
        f.showturtle()
        d.showturtle()
        b.showturtle()


    #t.CloseGame()
    def stoprun():
        gameover()
        scr.bye()

    #---Executing.Prep---#

    #t.Keybinds()
    scr.listen()

    scr.onkey(go_up, "Up")
    scr.onkey(go_down, "Down")
    scr.onkey(go_left, "Left")
    scr.onkey(go_right, "Right")

    scr.onkey(go_up, "w")
    scr.onkey(go_down, "s")
    scr.onkey(go_left, "a")
    scr.onkey(go_right, "d")

    scr.onkey(stoprun, "Escape")

    #-------Main.Loop--------#
    while True:
        scr.update()

        #t.BorderCon()
        if h.xcor() > 290 or h.xcor() < -290 or h.ycor() > 290 or h.ycor() < -290:
            gameover()

        #t.FoodGopGop()
        if h.distance(f) < 20 or h.distance(d) < 20:
            
            #t.Gridding()
            fx = snap(r.randint(-280, 280))
            fy = snap(r.randint(-280, 280))
            f.goto(fx, fy)
            
            dx = snap(r.randint(-280, 280))
            dy = snap(r.randint(-280, 280))
            d.goto(dx, dy)
            
            bx = snap(r.randint(-280, 280))
            by = snap(r.randint(-280, 280))
            b.goto(bx, by)
            
            score = score + 1

            #t.NewScoring()
            p.clear()
            p.goto(0, 267)
            p.write(f"Score: {score} | Highscore: {high_score}", align="center", font=("Monospace", 20, 'bold'))
            scr.update()

        #t.Boom()
        if h.distance(b) < 20:
            
            #t.Fire()
            b.color("#FF8000")
            
            #t.Devestated()
            for i in range(1, 10):
                h.shapesize(i, i)
                b.shapesize(i * 1.5, i * 1.5)
                
                #t.Destruction()
                if i % 2 == 0:
                    h.color("yellow")
                    scr.bgcolor("red")
                else:
                    h.color("orange")
                    scr.bgcolor("black")
                
                scr.update()
                ti.sleep(0.05)
            
            #t.Calmation()
            h.shapesize(1, 1)
            b.shapesize(1, 1)
            scr.bgcolor("#FACA72")
            gameover()

        move()
        ti.sleep(0.067)

#---snakegame---#
def snakegame():
    #---setup---#

    #t.Screen()
    scr = t.Screen()
    scr.title("Snake Game")
    scr.bgcolor("#0CB114")
    scr.setup(600, 600)
    scr.tracer(0)

    #t.ScoreDef()
    global score, high_score

    #t.head()
    h = t.Turtle()
    h.shape('square')
    h.color("#ffdd00")
    h.penup()
    h.speed(0)
    h.showturtle()
    h.direction = 'stop'
    body = []

    #t.food()
    f = t.Turtle()
    f.shape('circle')
    f.penup()
    f.color("#07B3B9")
    f.speed(0)
    f.showturtle()
    f.direction = 'stop'
    f.goto(0, 60)

    #t.GoldenBlueberry()
    fg = t.Turtle()
    fg.shape('circle')
    fg.penup()
    fg.color("#FFD700")
    fg.speed(0)
    fg.hideturtle()
    fg.goto(1000, 1000)

    #t.pen()
    p = t.Turtle()
    p.color("#171717")
    p.hideturtle()
    p.penup()
    p.direction = 'stop'
    p.goto(0, 267)
    p.write(f"Score: 0 | Highscore: 0", align= "center", font= ("Monospace", 20, 'bold'))

    #-----Functions--------#

    #t.Move()
    def move():
        if h.direction == "up":
            y = h.ycor()
            h.sety(y+20)
        
        if h.direction == "down":
            y = h.ycor()
            h.sety(y-20)

        if h.direction == "left":
            x = h.xcor()
            h.setx(x-20)

        if h.direction == "right":
            x = h.xcor()
            h.setx(x+20)

    #t.Controls()
    def go_up():
        if h.direction != "down":
            h.direction = "up"
    def go_down():
        if h.direction != "up":
            h.direction = "down"
    def go_left():
        if h.direction != "right":
            h.direction = "left"
    def go_right():
        if h.direction != "left":
            h.direction = "right"

    #t.GameOver()
    def gameover():
        #t.Endgame()
        h.hideturtle()
        f.hideturtle()
        fg.hideturtle()

        ti.sleep(0.5)
        p.clear()
        p.goto(0, 0)
        p.write("Game Over!", align= "center", font= ("Monospace", 20, 'bold'))
        scr.update()
        p.clear()
        ti.sleep(1)

        #t.RestartAnimation()
        p.clear()
        p.write("Restarting", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.3)
        
        p.clear()
        p.write("Restarting.", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.3)
        
        p.clear()
        p.write("Restarting..", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.3)
        
        p.clear()
        p.write("Restarting...", align="center", font=("Monospace", 20, 'bold'))
        scr.update()
        ti.sleep(0.67)
        
        #t.NewScoring()
        global score, high_score
        p.clear()
        p.goto(0, 267)

        if score > high_score:
            high_score = score
        score = 0
        p.write(f"Score: {score} | Highscore: {high_score}", align="center", font=("Monospace", 20, 'bold'))
        scr.update()

        h.goto(0, 0)
        h.direction = 'stop'

        f.goto(0, 60)
        fg.goto(1000, 1000)

        h.showturtle()
        f.showturtle()

        for i in body:
            i.goto(1000, 1000)
        body.clear()

    #t.CloseGame()
    def stoprun():
        gameover()
        scr.bye()


    #-----Executing.Prep-------#

    #t.Keybinds()
    scr.listen()

    scr.onkey(go_up, "Up")
    scr.onkey(go_down, "Down")
    scr.onkey(go_left, "Left")
    scr.onkey(go_right, "Right")

    scr.onkey(go_up, "w")
    scr.onkey(go_down, "s")
    scr.onkey(go_left, "a")
    scr.onkey(go_right, "d")

    scr.onkey(stoprun, "Escape")

    #-------Main.Loop--------#
    while True:
        scr.update()

        #t.BorderCon()
        if h.xcor() > 290 or h.xcor() < -290 or h.ycor() > 290 or h.ycor() < -290:
            gameover()

        #t.FoodGopGop()
        if h.distance(f) < 20:
            fx = snap(r.randint(-280, 280))
            fy = snap(r.randint(-280, 280))
            f.goto(fx, fy)
            score = score + 1

            #t.fgShow()
            if score % 5 == 0:
                fgx = snap(r.randint(-270, 270))
                fgy = snap(r.randint(-270, 270))
                fg.goto(fgx, fgy)
                fg.showturtle()

            #t.NewScoring()
            p.clear()
            p.goto(0, 267)
            p.write(f"Score: {score} | Highscore: {high_score}", align="center", font=("Monospace", 20, 'bold'))
            scr.update()

            #t.GrowthAfterGopGop()
            bodee = t.Turtle("square")
            bodee.color("#ffff79")
            bodee.penup()
            bodee.speed(0)
            body.append(bodee)

        #t.fgGopGop()
        if h.distance(fg) < 20:
            fg.hideturtle()
            fg.goto(1000, 1000)
            score += 3
            p.clear()
            p.goto(0, 267)
            p.write(f"Score: {score} | Highscore: {high_score}", align="center", font=("Monospace", 20, 'bold'))
            
            #t.GoldenTail()
            for _ in range(3):
                bodee = t.Turtle('square')
                bodee.color("#ffd500")
                bodee.penup()
                body.append(bodee)

        #t.KilBilTail()
        for m in range(len(body)-1, 0, -1):
            x = body[m-1].xcor()
            y = body[m-1].ycor()
            body[m].goto(x, y)

        #t.AttachedTail()
        if len(body) > 0:
            x = h.xcor()
            y = h.ycor()
            body[0].goto(x, y)
        
        move()

        #t.TailGopGop()
        for w in body:
            if w.distance(h) < 10:
                gameover()

        ti.sleep(0.067)

#---menuscreen---#
def drawmenu():
    scr = t.Screen()

    #t.Menu()
    scr.clear() 
    scr.title("Python Games")
    scr.bgcolor("#72C8FA")
    scr.setup(600, 600)
    scr.tracer(0)

    #t.Button()
    btn_ant = t.Turtle()
    btn_ant.shape("square")
    btn_ant.resizemode("user")
    btn_ant.shapesize(stretch_wid=2, stretch_len=10, outline=5) 
    btn_ant.color("black", "#FFFF00")
    btn_ant.penup()
    btn_ant.goto(0, 20)

    btn_snake = t.Turtle()
    btn_snake.shape("square")
    btn_snake.resizemode("user")
    btn_snake.shapesize(stretch_wid=2, stretch_len=10, outline=5)
    btn_snake.color("black", "#00ffbb")
    btn_snake.penup()
    btn_snake.goto(0, -60)

    #t.Logo()
    logo = t.Turtle()
    logo.hideturtle()
    logo.penup()
    logo.color("#171717")
    logo.goto(0, 150)
    logo.write("PYGAMES", align="center", font=("Monospace", 40, "bold"))
    logo.goto(0, 120)
    logo.write(":Select Your Mode:", align="center", font=("Monospace", 15, "italic"))

    #t.ButtonFunc()
    def click_ant(x, y):
        btn_ant.onclick(None)
        scr.clear()
        antgame()

    def click_snake(x, y):
        btn_snake.onclick(None)
        scr.clear()
        snakegame()

    #t.Click()
    btn_ant.onclick(click_ant)
    btn_snake.onclick(click_snake)
    
    scr.update()
    scr.mainloop()

drawmenu()