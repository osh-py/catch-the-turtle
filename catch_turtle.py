import turtle
import random
import time
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch Turtle")
score = turtle.Turtle()
score.color("Blue")
score.teleport(0.00,360)
score.hideturtle()
timer = turtle.Turtle()
timer.hideturtle()
timer.teleport(0.00,330)
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.shapesize(1.5)
kaplumbaga.color("Green")
kaplumbaga.up()
count = 0 
zaman = 10

score.write(f"Score : {count}", align="Center", font=("Arial", 20, "bold"))
timer.write(f"Timer : {zaman}", align="Center", font=("Arial", 20, "bold"))

def click(x,y):
        global count
        count+=1
        score.clear()
        score.write(f"Score : {count}", align="Center", font=("Arial", 20, "bold"))

while 0<zaman:
    time.sleep(0.3)
    timer.clear()
    timer.write(f"Timer : {zaman}", align="Center", font=("Arial", 20, "bold"))
    zaman-=1
    if zaman==0:
        timer.clear()
        timer.write(f"Game Over!", align="Center", font=("Arial", 20, "bold"))

    kaplumbaga.hideturtle()
    rastgeleX = random.randint(0,350)
    rastgeleY = random.randint(0,350)
    kaplumbaga.teleport(rastgeleX,rastgeleY)
    time.sleep(0.7)
    kaplumbaga.showturtle()
    kaplumbaga.onclick(click, 1)
print("\nOyun bitti")

kaplumbaga.onclick(lambda x,y: score.clear(),1)
kaplumbaga.onclick(lambda x,y: score.write(f"Score : {count}", align="Center", font=("Arial", 20, "bold")),1)
kaplumbaga.teleport(0.00,0.00)





turtle.done()