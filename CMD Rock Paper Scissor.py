import random
import subprocess

your_score = 0
bot_score = 0
win = ['rs', 'pr', 'sp']
draw = ['rr', 'pp', 'ss']
you = ''
bot = ''
result = ''
decrypt = {'r':'Rock','p':'Paper','s':'Scissor','':''}

def your_choice(prompt):
    while True:
        answer = input(prompt)
        try:
            if answer in ('r','p','s','e'):
                return answer
        except: pass

def display_score():
    global your_score , bot_score , you , bot
    print(f"    >>> You: {your_score} - {bot_score} :Bot <<<")
    print("-------------------------------")
    print(f"You chose: {decrypt[you]} - Bot chose: {decrypt[bot]}")
    print(f"Result: {result}")

display_score()
while True:
    bot = random.choice(['r','p','s'])
    you = your_choice('You choose (r or p or s): '
                      '\nOr press [e]xit to quit out: ')
    if you != 'e':
        if "".join([you,bot]) in win:
            your_score += 1
            result = "You win"
        elif "".join([you,bot]) in draw:
            result = "Draw"
        else:
            bot_score += 1
            result = "You lose"
        subprocess.run("cls",shell= True)
        display_score()
    else: exit()