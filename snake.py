from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 650
SPEED = 30
SPACE_SIZE = 30
BODY_PARTS = 4
SNALE_COLOR = 'Orange'
FOOD_COLOR = 'RED'
BACKGROUND_COLOR = 'BLACK'

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range (0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x + SPACE_SIZE,y+ SPACE_SIZE,fill=SNALE_COLOR,tags="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0,int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x + SPACE_SIZE,y + SPACE_SIZE,fill=FOOD_COLOR,tag="food")
def next_turn(snake,food):

    x,y=snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNALE_COLOR)
    snake.squares.insert(0,square)
    if x==food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete('food')
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED,next_turn,snake,food)
def change_directions(new_directions):
    global direction
    if new_directions == 'left':
        if direction != 'right':
            direction = new_directions
    elif new_directions == 'right':
        if direction != 'left':
            direction = new_directions
    elif new_directions == 'up':
        if direction != 'down':
            direction = new_directions
    elif new_directions == 'down':
        if direction != 'up':
            direction = new_directions
def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>= GAME_WIDTH:
        return TRUE
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game over")
        return TRUE

    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y == body_part[1]:
            print('Game Over')
            return TRUE
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_screenheight()/2,font=('consolas',70),text='Game Over',fill='Red',tag='Game Over')

window = Tk()
window.title("Snek game")
window.resizable(False,False)

score = 0
direction = 'down'

label = Label(window, text='Score:{}'.format(score),font=('consolas',40))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda event: change_directions('left'))
window.bind('<Right>',lambda event: change_directions('right'))
window.bind('<Up>',lambda event: change_directions('up'))
window.bind('<Down>',lambda event: change_directions('down'))

snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()