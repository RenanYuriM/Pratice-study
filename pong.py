import turtle
import os




def play_pong():  # function that runs the game
    wn = turtle.Screen()        # Created a window view
    wn.title("Pong by Hand")    # Game title
    wn.bgcolor("black")         # Background color
    wn.setup(width=800, height=600) # Screen size
    wn.tracer(0)                # The game is going fluidly

    # Paddle A, the attributes of the paddle on the left.
    paddle_l = turtle.Turtle() 
    paddle_l.speed(0)
    paddle_l.shape("square")  
    paddle_l.color("white")
    paddle_l.shapesize(stretch_wid=5, stretch_len=1)
    paddle_l.penup()
    paddle_l.goto(-350, 0)

    # Paddle B, The attributes of the paddle on the right.
    paddle_r = turtle.Turtle()
    paddle_r.speed(0)
    paddle_r.shape("square")
    paddle_r.color("white")
    paddle_r.shapesize(stretch_wid=5, stretch_len=1)
    paddle_r.penup()
    paddle_r.goto(350, 0)

    # Ball, The attributes of the ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2 
    ball.dy = -2

    # Pen, The attributes of the pen.
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player L: 0 PlayerR: 0", align="center", font=("Courier", 24, "normal"))

    #Score L

    score_l = 0

    #Score R

    score_r = 0


    def paddle_l_up():
        y = paddle_l.ycor() # ycor = how the "turtle" give coordinate
        y += 20             # add 20 pixel to the y coordinates
        paddle_l.sety(y)    # set the new ‘y’ coordinate

    def paddle_l_down():
        y = paddle_l.ycor()
        y -= 20 
        paddle_l.sety(y) 


    def paddle_r_up():
        y = paddle_r.ycor()
        y += 20
        paddle_r.sety(y)
        

    def paddle_r_down():
        y = paddle_r.ycor()
        y -= 20
        paddle_r.sety(y)
    

    # Keyboard binding

    wn.listen()     # When the user presses a specific key, it instructs the program to perform an action.
    wn.onkeypress(paddle_l_up, "w") 
    wn.onkeypress(paddle_l_down, "s") 
    wn.onkeypress(paddle_r_up, "Up") 
    wn.onkeypress(paddle_r_down, "Down") 

    # Main game loop
    while True:
        wn.update()     


        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)    

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay barulho.wav&")
        # Border checking
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay barulho.wav&")
        # Border checking
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_l += 1
            pen.clear()
            pen.write("Player L: {} Player R: {}".format(score_l, score_r), align="center", font=("Courier", 24, "normal"))
        # Border checking
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_r += 1
            pen.clear()
            pen.write("Player L: {} Player R: {}".format(score_l, score_r), align="center", font=("Courier", 24, "normal"))

        # Collisions between the paddle and the ball on the right side.
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            os.system("afplay barulho.wav&")

        # Collisions between the paddle and the ball on the left side.
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
        

# Function to start the game.
def start_game():
    # close menu 
    start_button.clear()
    # Start the gaming
    play_pong()

# Menu screen setup.
menu_screen = turtle.Screen()
menu_screen.title("Menu Inicial")
menu_screen.bgcolor("black")

# Create the 'Press SPACE to Start' button on the menu screen.
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("green")
start_button.penup()
start_button.hideturtle()
start_button.goto(0, 0)
start_button.write("Pressione ESPAÇO para Iniciar", align="center", font=("Courier", 24, "normal"))

# Keyboard binding to start the game.
menu_screen.listen()
menu_screen.onkeypress(start_game, "space")

# Keeps the menu screen open.
menu_screen.mainloop()
