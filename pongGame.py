import turtle
# python feature like a drawing board


window = turtle.Screen()
window.title("pong game")
window.bgcolor("#ffe6cc")
window.setup(width=800, height=600)
window.tracer(0)
# stop the window from updating

#score calc
score_a =0
score_b =0


# paddle a
a = turtle.Turtle() # turtle object
a.speed(0)
a.shape("square")
a.color("#b3d9ff")
a.shapesize(stretch_wid=5, stretch_len=1)
a.penup()  # prevent the turtle draw a line
a.goto(-350,0) # set board A in place

# paddle b
b = turtle.Turtle() # turtle object
b.speed(0)
b.shape("square")
b.color("#b3ffb3")
b.shapesize(stretch_wid=5, stretch_len=1)
b.penup()  # prevent the turtle draw a line
b.goto(350,0) # set board A in place

# ball

ball = turtle.Turtle() # turtle object
ball.speed(0)
ball.shape("circle")
ball.color("#e6b3ff")
ball.penup()  # prevent the turtle draw a line
ball.goto(0,0) # set board A in place
# every time the ball is move its will move with 2 pixel
ball.dx = 0.5
ball.dy = -0.5

# score
score = turtle.Turtle()
score.speed(0)
score.color("#ffb3d9")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("blue player score :0 | green player score :0", align="center", font=("Courier",20,"normal"))


# function

def paddle_A_up():
    y = a.ycor()  # return the y coordinate
    y += 20
    a.sety(y)


def paddle_A_down():
    y = a.ycor()  # return the y coordinate
    y -= 20
    a.sety(y)


def paddle_B_up():
    y = b.ycor()  # return the y coordinate
    y += 20
    b.sety(y)

def paddle_B_down():
    y = b.ycor()  # return the y coordinate
    y -= 20
    b.sety(y)

# keyboard
# listen to keyboard input
window.listen()
window.onkeypress(paddle_A_up, "w")  # what to do when the user click on w
window.onkeypress(paddle_A_down, "s")  # what to do when the user click on s
window.onkeypress(paddle_B_up, "Up")  # what to do when the user click on w
window.onkeypress(paddle_B_down, "Down")  # what to do when the user click on s



# main game loop
# update the screen in each loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor()+ball.dx) # move in 2 pixels to the side
    ball.sety(ball.ycor()+ball.dy) # move in 2 pixels to the up

    # border checking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1 # revers the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # revers the direction


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1 # paddle 1 get point because we in the right side of the screen
        score.clear()
        score.write("blue player score :{} | green player score :{}".format(score_a, score_b), align="center",font=("Courier", 20, "normal"))  # update the score in the screen

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1 # # paddle 2 get point because we in the left side of the screen
        # score.write("blue player score :{} | green player score :{}".format(score_a,score_b), align="center", font=("Courier", 20, "normal")) # update the score in the screen

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor()< b.ycor() + 40  and ball.ycor() > b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< a.ycor() + 40  and ball.ycor() > a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

