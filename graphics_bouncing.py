# import pygame library and initialize game engine 
import pygame
pygame.init() 

# define colors 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# open a new window 
width = 640
height = 480
size = (width, height) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Graphics Window")

# boolean to determine whether to continue running 
carryOn = True 

# clock to control how fast the screen updates 
clock = pygame.time.Clock() 

rect1 = [50, 200, 40, 40]
rect2 = [300, 50, 40, 40]

rect1vx = 6
rect2vy = 8

# ---------- Main Program Loop ----------
while carryOn: 
    # --- Main event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False 

    # --- Game logic 
    rect1[0] += rect1vx
    rect2[1] += rect2vy
    if rect1[0] + 40 >= width or rect1[0] <= 0:
        rect1vx *= -1
    if rect2[1] + 40 >= height or rect2[1] <= 0:
        rect2vy *= -1

    # --- Drawing onto screen 
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rect1)
    pygame.draw.rect(screen, GREEN, rect2)

    # --- Update screen 
    pygame.display.flip() 

    # --- Limit frames per second 
    clock.tick(30)


# after exiting the main program loop, stop the game engine
pygame.quit() 