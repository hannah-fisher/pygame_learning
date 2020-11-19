# import pygame library and initialize game engine 
import pygame
pygame.init() 

# define colors 
WHITE = (255, 255, 255)

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

# ---------- Main Program Loop ----------
while carryOn: 
    # --- Main event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False 

    # --- Game logic 

    # --- Drawing onto screen 
    screen.fill(WHITE)

    # --- Update screen 
    pygame.display.flip() # presumably this is using a double buffer, switches side to read while other side is filled 

    # --- Limit frames per second 
    clock.tick(30)


# after exiting the main program loop, stop the game engine
pygame.quit() 