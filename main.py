from tkinter import *
import random

#game variables
game_width=500
game_height=500
game_speed=150
space_size=50
body_parts=2
snake_colour="blue"
food_colour="red"
background_colour="black"

class Snake:
     def __init__(self):
        #self.body_size=body_parts
        self.coordinates=[]
        self.squares=[]

        for i in range(0, body_parts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y, x+space_size, y+space_size, fill=snake_colour)
            self.squares.append(square)

class Food:
     def __init__(self):
        x = random.randint(0, int(game_width/space_size)-1) * space_size
        y= random.randint(0, int(game_height/space_size)-1) * space_size

        self.coordinates=[x,y]
        canvas.create_oval(x,y, x+space_size, y+space_size, fill=food_colour, tag="food")

def next_turn(snake,food):

    #unpacking snake head
     x, y= snake.coordinates[0]

     if direction=="up":
         y-=space_size
     
     elif direction=="down":
        y+=space_size
     
     elif direction=="left":
         x-=space_size
     
     elif direction=="right":
         x+=space_size

     snake.coordinates.insert(0,(x,y))

     square=canvas.create_rectangle(x,y, x+space_size, y+space_size, fill=snake_colour)

     snake.squares.insert(0,square)

    #updating score on eating food
     if x==food.coordinates[0] and y==food.coordinates[1]:
         global score
         score+=1
         lable.config(text="Score:{}".format(score))

         canvas.delete("food")
         food=Food()

     else:
        #after unpacking snake head deleting its extra body parts
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
     #snkae crashes in boundry or itself; gameover
     if check_collision(snake):
        game_over()
     
     #if not snake continue to move 
     else:
        window.after(game_speed, next_turn, snake, food)
    
def change_direction(new_direction):
    
    #assigning keys to move snake
    global direction

    if new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

    elif new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

def check_collision(snake):
     
     x,y=snake.coordinates[0]

     #snake collides in boundries
     if x<0 or x>=game_width:
        return True
     elif y<0 or y>=game_height:
        return True
     #snake collidies with himslef
     for i in snake.coordinates[1:]:
        if x==i[0] and y==i[1]:
            return True
    
     return False

def game_over():
     canvas.delete(ALL)
     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas",50), text="GAME OVER", fill="red")     

#creating window
window=Tk()
window.title("Snake Game")

window.resizable(False, False) # game window won't be able resized

score=0
direction="down"

lable=Label(window, text="Score:{}".format(score), font=('consolas',30))
lable.pack()

canvas=Canvas(window, bg=background_colour, height=game_height, width=game_width)
canvas.pack()

#to bring window in center
window.update()

window_height= window.winfo_height()
window_width= window.winfo_width()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

x=int((screen_width/2) - (window_width/2))
y=int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#binding keys
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

#Calling Classes and Functions
snake=Snake()
food=Food()
next_turn(snake,food)

window.mainloop()
