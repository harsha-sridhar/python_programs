from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
print("Instructions:\n\"w\" - Move forward\n\"s\" - Move backward\n\"a\" - Move Left\n\"d\" - Move Right\n\"c\" - Clear the screen")
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear_drawing,"c")
screen.exitonclick()