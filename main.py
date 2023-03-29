from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.title("Turtle Race")
screen.bgcolor("black")
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

y= -150

for turtle_index in range(6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[turtle_index])
    my_turtle.penup()
    my_turtle.goto(-230, y)
    y += 60
    all_turtles.append(my_turtle)

if user_bet:
    is_race_on = True
    

while is_race_on:
    
    for turtle in all_turtles:
        
        if turtle.xcor() > 230:
            
            is_race_on = False
            winning_color = turtle.pencolor()
            
            if user_bet == winning_color:
                print(f"You've Won! {winning_color} is the winning color")
                
            else:
                
                print(f"You've Lost! {winning_color} is the winning color")
            break
        
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)

screen.exitonclick()