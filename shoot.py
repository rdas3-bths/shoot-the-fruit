import pgzrun
from random import randint
from pgzero.builtins import Actor

apple = Actor("apple")
text = "Shoot the Fruit!"
score = 0


def place_apple():
    apple.x = randint(20, 700)
    apple.y = randint(20, 500)


def draw():
    screen.clear()
    screen.draw.text(text, topleft=(10, 10))
    apple.draw()


def on_mouse_down(pos):
    global score
    global text
    if apple.collidepoint(pos):
        text = "Good shot"
        score = score + 1
        text = text + "\nScore: " + str(score)
        place_apple()
    else:
        text = "Bad shot"
        quit()


place_apple()
pgzrun.go()


