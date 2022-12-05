from tkinter import *
from tkinter import ttk
import random

you_score = 0
bot_score = 0

def reset():
    global you_score , bot_score
    you_score = 0
    bot_score = 0
    label_status.configure(text="------")
    label_score.configure(text="-")
    label_you.configure(image=image_default_)
    label_bot.configure(image=image_default_)

def btn_click(button):
    global you_score , bot_score
    you = button
    bot = random.choice(['r', 'p', 's'])
    label_you.configure(image=dict_btn[you][0])
    label_bot.configure(image=dict_btn[bot][1])
    if you + bot in ['rs', 'pr', 'sp']:
        you_score +=1
        label_status.configure(text=f"You win")
    elif you + bot in ['rr', 'pp', 'ss']:
        label_status.configure(text=f"Draw")
    else:
        bot_score +=1
        label_status.configure(text=f"You lose")
    label_score.configure(text=f"{you_score} - {bot_score}")

# =============================================
win = Tk()
win.title("Rock-Paper-Scissor")
win.geometry("400x300")
win.resizable(0,0)
win.iconbitmap(r"footages\paper.ico")

image_vs = PhotoImage(file=r"footages\vs.png").subsample(8,8)
a = 4
image_rock_flip_ = PhotoImage(file=r"footages\rock.png").subsample(-a,a)
image_paper_flip_ = PhotoImage(file=r"footages\paper.png").subsample(-a,a)
image_scissor_flip_ = PhotoImage(file=r"footages\scissor.png").subsample(-a,a)
image_rock_ = PhotoImage(file=r"footages\rock.png").subsample(a)
image_paper_ = PhotoImage(file=r"footages\paper.png").subsample(a)
image_scissor_ = PhotoImage(file=r"footages\scissor.png").subsample(a)
image_default_ = PhotoImage(file=r"footages\default.png").subsample(a)
b = 10
image_rock = PhotoImage(file=r"footages\rock.png").subsample(b)
image_paper = PhotoImage(file=r"footages\paper.png").subsample(b)
image_scissor = PhotoImage(file=r"footages\scissor.png").subsample(b)
image_default = PhotoImage(file=r"footages\default.png").subsample(b)
image_reset = PhotoImage(file=r"footages\reset.png").subsample(13)

dict_btn = {'r':[image_rock_,image_rock_flip_],'p':[image_paper_,image_paper_flip_],'s':[image_scissor_,image_scissor_flip_]}

label_score = Label(win,text="-",font=("Seven Segment",25,"bold"))
label_score.pack(pady=10)

btn_reset = ttk.Button(win,text="RESET",command= reset)
btn_reset.place(x=300,y=256)
#-----------------------------------------------
frm_status = Frame(win)
frm_status.pack()
label_you = Label(frm_status,text="YOU",font=("Arial",10,"bold"),foreground="white",background="#db2128")
label_you.pack(side=LEFT)
label_status = Label(frm_status,text="------",font=("Arial",15,"bold"),foreground="black",width=15)
label_status.pack(side=LEFT)
label_bot = Label(frm_status,text="BOT",font=("Arial",10,"bold"),foreground="white",background="#1d77bd")
label_bot.pack(side=LEFT)

frm_vs = Frame(win)
frm_vs.pack()
label_you = Label(frm_vs,image=image_default_)
label_you.grid(row=0,column=0)
label_vs = Label(frm_vs,image=image_vs)
label_vs.grid(column=1,row=0)
label_bot = Label(frm_vs,image=image_default_)
label_bot.grid(column=2,row=0)

label_btn = Label(win,relief=RIDGE)
label_btn.pack(pady=5)
btn_rock = Button(label_btn,image=image_rock,borderwidth=0,command= lambda :btn_click('r'))
btn_rock.grid(row=0,column=0,padx=5)
btn_paper = Button(label_btn,image=image_paper,borderwidth=0,command=lambda :btn_click('p'))
btn_paper.grid(row=0,column=1)
btn_scissor = Button(label_btn,image=image_scissor,borderwidth=0,command=lambda :btn_click('s'))
btn_scissor.grid(row=0,column=2,padx=5)
#-----------------------------------------------

win.mainloop()