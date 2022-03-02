import turtle as tu
import random
import time


score=0

with open("C:/Users/rajee/OneDrive/Documents/PYT/GAME 1/score_final.txt","r") as f:
    high_score=f.read()

def run_game():

    win = tu.Screen()
    win.title("Game_1")
    win.bgpic("C:/Users/rajee/OneDrive/Documents/PYT/GAME 1/GAME_MAIN/bot.png")
    win.tracer(0)

    pen = tu.Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()

    bar1 = tu.Turtle()
    bar1.speed(0)
    bar1.shape("square")
    bar1.color("blue")
    bar1.shapesize(3, 1)
    bar1.penup()
    bar1.goto(-350, 0)
    bar1.dy = 0.1

    ball = tu.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.shapesize(2, 2)
    ball.penup()
    ball.goto(500, 0)
    ball.dx = -.8
    ball.dy = 0

    ball2 = ball.clone()
    ball2.goto(600, 100)

    ball3 = ball.clone()
    ball3.goto(600, -100)

    ball4 = ball.clone()
    ball4.goto(750, 200)

    ball5 = ball.clone()
    ball5.goto(750, -200)

    ball6 = ball.clone()
    ball6.goto(400, 240)

    ball7 = ball.clone()
    ball7.goto(400, -240)

    def bar1_up():
        y = bar1.ycor()
        y += 40
        bar1.sety(y)


    def bar1_down():
        y = bar1.ycor()
        y -= 40
        bar1.sety(y)


    def ball_move():
        ball.clear()

    
    win.listen()
    win.onkeypress(bar1_up, "w")
    win.onkeypress(bar1_down, "s")


    def move_ball():

        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        ball2.setx(ball2.xcor()+ball2.dx)
        ball2.sety(ball2.ycor()+ball2.dy)

        ball3.setx(ball3.xcor()+ball3.dx)
        ball3.sety(ball3.ycor()+ball3.dy)

        ball4.setx(ball4.xcor()+ball4.dx)
        ball4.sety(ball4.ycor()+ball4.dy)

        ball5.setx(ball5.xcor()+ball5.dx)
        ball5.sety(ball5.ycor()+ball5.dy)

        ball6.setx(ball6.xcor()+ball6.dx)
        ball6.sety(ball6.ycor()+ball6.dy)

        ball7.setx(ball7.xcor()+ball7.dx)
        ball7.sety(ball7.ycor()+ball7.dy)


    def ball1_move(incr):

        z = random.randint(500, 900)
        w = random.randint(0, 100)
        ball.setx(z)
        ball.sety(w)
        ball.setx(ball.xcor()+ball.dx+incr)
        ball.sety(ball.ycor()+ball.dy+incr)


    def ball2_move(incr):

        z = random.randint(500, 800)
        w = random.randint(120, 200)
        ball2.setx(z)
        ball2.sety(w)
        ball2.setx(ball2.xcor()+ball.dx+incr)
        ball2.sety(ball2.ycor()+ball.dy+incr)


    def ball3_move(incr):

        z = random.randint(500, 700)
        w = random.randint(220, 240)
        ball3.setx(z)
        ball3.sety(-w)
        ball3.setx(ball3.xcor()+ball.dx+incr)
        ball3.sety(ball3.ycor()+ball.dy+incr)


    def ball4_move(incr):

        z = random.randint(400, 800)
        w = random.randint(-100, 0)
        ball4.setx(z)
        ball4.sety(w)
        ball4.setx(ball4.xcor()+ball.dx+incr)
        ball4.sety(ball4.ycor()+ball.dy+incr)


    def ball5_move(incr):

        z = random.randint(400, 900)
        w = random.randint(-200,-120)
        ball5.setx(z)
        ball5.sety(-w)
        ball5.setx(ball5.xcor()+ball.dx+incr)
        ball5.sety(ball5.ycor()+ball.dy+incr)
    

    def ball6_move(incr):

        z = random.randint(400, 600)
        w = random.randint(-240, -220)
        ball6.setx(z)
        ball6.sety(-w)
        ball6.setx(ball6.xcor()+ball.dx+incr)
        ball6.sety(ball6.ycor()+ball.dy+incr)


    def ball7_move(incr):

        z = random.randint(450, 900)
        w = random.randint(-50,50)
        ball7.setx(z)
        ball7.sety(w)
        ball7.setx(ball7.xcor()+ball.dx+incr)
        ball7.sety(ball7.ycor()+ball.dy+incr)



    def restart_game(restart):
        if restart == "y":
            win.clearscreen()
            run_game()
        elif(restart == "n"):
            tu.bye()
        else:
            tu.bye()
           

    

    def game_end(score,high_score):
        pen.goto(0, 150)
        pen.clear()
        tu.clearscreen()
        win.bgpic("C:/Users/rajee/OneDrive/Documents/PYT/GAME 1/GAME_MAIN/bot.png")
        pen.write(f"Game Over\nYour Score = {score}", align="center", font=("Calibri", 20, "bold"))
        time.sleep(0.5)

        if (score > int(high_score)):
            
            high_score=score
            f = open('C:/Users/rajee/OneDrive/Documents/PYT/GAME 1/score_final.txt', 'w')
            f.write(str(score)+ " ")
            f.close()
            
        pen.goto(0,0)
        pen.write(f"HighScore = {high_score}", align="center", font=("Calibri", 20, "bold"))
        restart = win.textinput("Game result", "You lost \nDo you want to restart ? (y/n)")
        restart_game(restart)



    def main_game(score):
        while(True):

            win.update()
            move_ball()


            if(bar1.ycor() > 200):
                bar1.goto(-350, 200)
            elif(bar1.ycor() < -200):
                bar1.goto(-350, -200)

            if(ball.xcor() < -320 and ball.xcor() > -350 and ball.ycor() < bar1.ycor() + 50 and ball.ycor() > bar1.ycor() - 50):
                ball1_move(0)
                game_end(score,high_score)
            elif(ball.xcor() <-345):
                ball1_move(0.5)
                score += 10


            if(ball2.xcor() < -320 and ball2.xcor() > -350 and ball2.ycor() < bar1.ycor() + 50 and ball2.ycor() > bar1.ycor() - 50):
                ball2_move(0)
                game_end(score,high_score)
            elif(ball2.xcor() <-345):
                ball2_move(0.5)
                score += 10


            if(ball3.xcor() < -320 and ball3.xcor() > -350 and ball3.ycor() < bar1.ycor() + 50 and ball3.ycor() > bar1.ycor() - 50):
                ball3_move(0)         
                game_end(score,high_score)
            elif(ball3.xcor() <-345):
                ball3_move(0.5)
                score += 10


            if(ball4.xcor() < -320 and ball4.xcor() > -350 and ball4.ycor() < bar1.ycor() + 50 and ball4.ycor() > bar1.ycor() - 50):
                ball4_move(0)
                game_end(score,high_score)
            elif(ball4.xcor() <-345):
                ball4_move(0.5)
                score += 10


            if(ball5.xcor() < -320 and ball5.xcor() > -350 and ball5.ycor() < bar1.ycor() + 50 and ball5.ycor() > bar1.ycor() - 50):
                ball5_move(0)
                game_end(score,high_score)
            elif(ball5.xcor() <-345):
                ball5_move(0.5)
                score += 10

            if(ball6.xcor() < -320 and ball6.xcor() > -350 and ball6.ycor() < bar1.ycor() + 50 and ball6.ycor() > bar1.ycor() - 50):
                ball6_move(0)
                game_end(score,high_score)
            elif(ball6.xcor() <-345):
                ball6_move(0.5)
                score += 10

            if(ball7.xcor() < -320 and ball7.xcor() > -350 and ball7.ycor() < bar1.ycor() + 50 and ball7.ycor() > bar1.ycor() - 50):
                ball7_move(0)
                game_end(score,high_score)
            elif(ball7.xcor() <-345):
                ball7_move(0.5)
                score += 10


            pen.goto(0, 200)
            pen.clear()
            pen.write(f"Score = {score} , High Score = {high_score}", align="center",font=("Calibri", 20, "bold"))

    main_game(0)


run_game()
