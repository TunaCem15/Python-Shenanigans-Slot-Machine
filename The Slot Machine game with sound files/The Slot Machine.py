from turtle import *
from random import *
from time import sleep
from winsound import *
from math import *
money = 200
print("The slot machine is being generated. Please wait...")
bgcolor("hotpink")
speed(100)
color('red')
penup()
goto(100,100)
right(90)
pendown()
forward(210)
right(90)
forward(210)
right(90)
forward(210)
right(90)
forward(210)
right(180)
penup()
forward(140)
left(90)
pendown()
forward(210)
left(90)
penup()
forward(70)
left(90)
pendown()
forward(210)
color("aquamarine")
begin_fill()
right(90)
forward(70)
right(90)
forward(210)
right(90)
forward(70)
right(90)
forward(210)
end_fill()
left(90)
color("cyan")
begin_fill()
forward(70)
left(90)
forward(210)
left(90)
forward(70)
left(90)
forward(210)
end_fill()
penup()
left(90)
forward(70)
pendown()
color("darkslategray3")
begin_fill()
forward(70)
left(90)
forward(210)
left(90)
forward(70)
left(90)
forward(210)
end_fill()
penup()
goto(-45,-160)
pendown()
color('black')
write("Click the arrow below to play!", font = ("Arial", 20, "normal"))
penup()
goto(0,-220)
shapesize(10)
t1 = Turtle()
t1.penup()
t1.goto(-45,160)
t1.write("Click the arrow above to end the software!", font = ("Arial", 15, "normal"))
t1.penup()
t1.goto(0,220)
t1.shapesize(10)
t2 = Turtle()
t2.hideturtle()
t3 = Turtle()
t3.hideturtle()
t4 = Turtle()
t4.hideturtle()
t2.penup()
t3.penup()
t4.penup()
t2.goto(-70,15)
t3.goto(0,15)
t4.goto(70,15)
t8 = Turtle()
t8.penup()
t8.goto(-375,-200)
t8.shapesize(10)
t8.write("Click the arrow above to set a bet!", font = ("Arial", 15, "normal"))
t8.goto(-250,0)
num1 = None
num2 = None
num3 = None
t5 = Turtle()
t5.hideturtle()
t5.penup()
t5.goto(-280,200)
t6 = Turtle()
t6.hideturtle()
t6.penup()
t6.goto(280,-10)
t7 = Turtle()
t7.hideturtle()
t7.penup()
t7.goto(280,20)
t7.write("Money", font = ("Arial", 25, "normal"))
t6.write(money, font = ("Arial", 25, "normal"))
file_win = 'normal payout audio.wav'
file_jackpot = 'jackpot audio.wav'
file_loss = 'loss audio 2.wav'
bet_amount = None
bet_selected = False
bet_amount_selector = None
def roll(x,y):
    global num1,num2,num3, money,bet_amount,bet_selected
    if bet_selected == False:
        t2.write("You have didn't set a bet. Please try again.", font = ("Arial",12,"normal"))
        sleep(2)
        t2.clear()
    else:       
        num1 = randint(1,9)
        num2 = randint(1,9)
        num3 = randint(1,9)
        t2.write(num1, font = ("Arial", 15, "normal"))
        t3.write(num2, font = ("Arial", 15, "normal"))
        t4.write(num3, font = ("Arial", 15, "normal"))
        if num1 == num2 and num1 != num3:
            win_amount = floor(bet_amount*1.5)
            t5.write(f"Adjacent numbers! +{win_amount} dollars!", font = ("Arial", 10, "normal"))
            PlaySound(file_win, SND_FILENAME)
            money += win_amount
        elif num2 == num3 and num1 != num2:
            win_amount = floor(bet_amount*1.5)
            t5.write(f"Adjacent numbers! +{win_amount} dollars!", font = ("Arial", 10, "normal"))
            PlaySound(file_win, SND_FILENAME)
            money += win_amount
        elif num1 == num2 and num1 == num3:
            if bet_amount < 50:
                jackpot = floor(bet_amount * 8.5)
            elif bet_amount > 50 and bet_amount < 100:
                jackpot = floor(bet_amount * 6.5)
            else:
                jackpot = floor(bet_amount * 2.5)
            t5.write(f"Jackpot! +{jackpot} dollars!", font = ("Arial", 10, "normal"))
            PlaySound(file_jackpot, SND_FILENAME)
            money += jackpot
        else:
            t5.write(f"None! -{bet_amount} dollars!", font = ("Arial", 10, "normal"))
            PlaySound(file_loss, SND_FILENAME)
            money -= bet_amount
        sleep(0.5)
        t2.clear()
        t3.clear()
        t4.clear()
        t5.clear()
        t6.clear()
        t6.write(money, font = ("Arial", 25, "normal"))
def bet(x,y):
    global bet_amount, money, bet_selected, bet_amount_selector
    bet_amount_selector = int(input("Enter the amount you desire"))
    if bet_amount_selector > money:
        print("You can't bet more money than you have. Click the bet button again.")
        bet_amount_selector = None
    else:
        bet_amount = bet_amount_selector
        if bet_amount == 1:
            print("You betted 1 dollar")
            bet_selected = True
        else:
            print("You betted", bet_amount, "dollars")
            bet_selected = True
def close(x,y):
    exit()
onclick(roll)
t1.onclick(close)
t8.onclick(bet)
