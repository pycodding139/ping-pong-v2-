import tkinter as tk
import random

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Пинг-Понг")

        self.canvas = tk.Canvas(root, width=1500, height=900, bg="black")
        self.canvas.pack()

        self.paddle_a = self.canvas.create_rectangle(50, 150, 70, 200, fill="white")
        self.paddle_b = self.canvas.create_rectangle(430, 150, 450, 200, fill="white")
        self.ball = self.canvas.create_oval(230, 130, 250, 150, fill="white")

        self.ball_speed_x = random.choice([-1, 1]) * 2
        self.ball_speed_y = random.choice([-1, 1]) * 2

        self.root.bind("<KeyPress-Up>", self.move_paddle_a_up)
        self.root.bind("<KeyPress-Down>", self.move_paddle_a_down)
        self.root.bind("<KeyPress-w>", self.move_paddle_b_up)
        self.root.bind("<KeyPress-s>", self.move_paddle_b_down)

        self.score_a = 0
        self.score_b = 0
        self.score_display = self.canvas.create_text(250, 30, text="0 - 0", fill="white", font=("Helvetica", 16))

        self.update()

     def move_paddle_a_up(self, event):
        paddle_a_pos = self.canvas.coords(self.paddle_a)
        if paddle_a_pos[1] > 0:
            self.canvas.move(self.paddle_a, 0, -20)
        
    def move_paddle_a_down(self, event):
        paddle_a_pos = self.canvas.coords(self.paddle_a)
        if paddle_a_pos[3] < 300:
            self.canvas.move(self.paddle_a, 0, 20)

    def move_paddle_b_up(self, event):
        paddle_b_pos = self.canvas.coords(self.paddle_b)
        if paddle_b_pos[1] > 0:
            self.canvas.move(self.paddle_b, 0, -20)

    def move_paddle_b_down(self, event):
        paddle_b_pos = self.canvas.coords(self.paddle_b)
        if paddle_b_pos[3] < 300:
            self.canvas.move(self.paddle_b, 0, 20)


    def update(self):
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        ball_pos = self.canvas.coords(self.ball)

        if ball_pos[1] <= 0 or ball_pos[3] >= 300:
            self.ball_speed_y *= -1

        if ball_pos[0] <= 0:
            self.score_b += 1
            self.canvas.itemconfig(self.score_display, text=f"{self.score_a} - {self.score_b}")
            self.reset_ball()

        if ball_pos[2] >= 500:
            self.score_a += 1
            self.canvas.itemconfig(self.score_display, text=f"{self.score_a} - {self.score_b}")
            self.reset_ball()

        paddle_a_pos = self.canvas.coords(self.paddle_a)
        paddle_b_pos = self.canvas.coords(self.paddle_b)
        
        if ball_pos[0] <= paddle_a_pos[2] and paddle_a_pos[1] <= ball_pos[1] <= paddle_a_pos[3]:
            self.ball_speed_x *= -1
        
        if ball_pos[2] >= paddle_b_pos[0] and paddle_b_pos[1] <= ball_pos[1] <= paddle_b_pos[3]:
            self.ball_speed_x *= -1
        
        self.root.after(10, self.update)

    def reset_ball(self):
        self.canvas.coords(self.ball, 230, 130, 250, 150)
        self.ball_speed_x = random.choice([-1, 1]) * 2
        self.ball_speed_y = random.choice([-1, 1]) * 2

root = tk.Tk()
game = PongGame(root)
root.mainloop()
