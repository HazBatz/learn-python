from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, color, score):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                score.increase() #when the ball hits paddle then update score
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
             self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos [0] <= 0:
            self.x = 3
        if pos [2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def start_game(self,evt):
        self.started = True

class Score:
    def __init__(self, canvas, color):
        self.scoreValue = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.scoreValue, fill=color)

    def increase(self):
        self.scoreValue += 1
        self.canvas.itemconfig(self.id, text=self.scoreValue) #update text

tk = Tk()
tk.title('Bounce!')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red', score)
game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')

while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()

    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal', text='GAME OVER - score: ' + str(score.scoreValue))
        finished = True

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    if ball.hit_bottom == True:
        time.sleep(2) #wait 2 seconds
        break         #abort loop


# https://github.com/jasonrbriggs/python-for-kids/blob/main/ch12/bounce-11.py
#https://jasonrbriggs.com/python-for-kids-2/
