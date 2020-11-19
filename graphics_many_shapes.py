# import pygame library and initialize game engine 
import pygame
pygame.init() 

# define colors 
WHITE = (255, 255, 255)
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

# ---------- Main Program Loop ----------
while carryOn: 
    # --- Main event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False 

    # --- Game logic 

    # --- Drawing onto screen 
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [30, 80, 35, 50]) 
    pygame.draw.polygon(screen, BLUE, [(100, 80), (135, 140), (170, 80)])
    pygame.draw.polygon(screen, BLUE, [(200, 100), (200, 120), (220, 140), (240, 140), (260, 120), (260, 100), (240, 80), (220, 80)])
    pygame.draw.circle(screen, BLUE, (320, 115), 30)
    pygame.draw.ellipse(screen, BLUE, [380, 90, 90, 50])

    # --- Update screen 
    pygame.display.flip() 

    # --- Limit frames per second 
    clock.tick(30)


# after exiting the main program loop, stop the game engine
pygame.quit() 