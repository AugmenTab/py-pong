import os
import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Controls
screen_boundary = 240


def paddle_a_up():
    y = paddle_a.ycor()
    if y != screen_boundary:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y != -screen_boundary:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y != screen_boundary:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y != -screen_boundary:
        y -= 20
        paddle_b.sety(y)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('PlayerA: 0 | PlayerB: 0', align='center', font=('Courier', 24, 'normal'))

# Score
score_a = 0
score_b = 0

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Other Functions
def bounce():
    print('\a')


def handle_score():
    pen.clear()
    pen.write('PlayerA: {} | PlayerB: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
    os.system('aplay ./announcer/ball-reset.wav&')


def difficulty_up():
    ball.dx *= 1.05
    ball.dy *= 1.05


# Main Game Loop
os.system('aplay ./announcer/oddball.wav')
os.system('aplay ./announcer/play-ball.wav&')
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Movement
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce()
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce()
    if ball.xcor() > 390:
        score_a += 1
        difficulty_up()
        handle_score()
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        score_b += 1
        difficulty_up()
        handle_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Collisions
    if (340 < ball.xcor() < 350) and \
            (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        bounce()
    if (-340 > ball.xcor() > -350) and \
            (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        bounce()
