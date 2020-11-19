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

circleX = 320
circleY = 240 

# ---------- Main Program Loop ----------
while carryOn: 
    # --- Main event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False 

    # --- Game logic
    (x, y) = pygame.mouse.get_pos()

    if circleX < x - 2:
        circleX += 4
    elif circleX > x + 2:
        circleX -= 4
    if circleY < y - 2:
        circleY += 4
    elif circleY > y + 2:
        circleY -= 4

    # --- Drawing onto screen 
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), 30)
    pygame.draw.circle(screen, GREEN, (circleX, circleY), 20)

    # --- Update screen 
    pygame.display.flip() 

    # --- Limit frames per second 
    clock.tick(30)


# after exiting the main program loop, stop the game engine
pygame.quit() 