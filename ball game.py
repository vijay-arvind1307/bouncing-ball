import turtle

# Create screen
sc = turtle.Screen()
sc.title("BOUNCING BALL")
sc.bgcolor("black")
sc.setup(width=500, height=650)

#create padddle
paddle=turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("red")
paddle.shapesize(stretch_wid=1, stretch_len=8)
paddle.penup()
paddle.goto(0,-250)


#create ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy =-5

# Display the title
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("BOUNCING BALL",align="center", font=("Courier", 24, "normal"))

def paddle_right():
    if paddle.xcor()<180:
        paddle.goto(paddle.xcor()+50, paddle.ycor())

def paddle_left():
    if paddle.xcor()>= -150:
        paddle.goto(paddle.xcor()-50, paddle.ycor())

sc.listen()
sc.onkeypress(paddle_right, 'Right')
sc.onkeypress(paddle_left, 'Left')

def move_ball():
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)
   
    # Change dx if ball gets to either side
    if ball.xcor() >=230 or ball.xcor()<= -240:
        ball.dx *= -1

    # Change dy if ball gets to top
    if ball.ycor() >= 290:
        ball.dy *= -1

    # Reset ball to middle if out on the bottom
    if ball.ycor() <= -280:
        ball.goto(0,0)
        ball.dy *= -1
        
# Bounce on paddle
def ball_bounce():
        if ball.dy<0 and ball.ycor()<=-245 and (paddle.xcor()-60 <= ball.xcor() <= paddle.xcor()+60):
                ball.dy *= -1

while True:
    sc.update()
    move_ball()
    ball_bounce()
