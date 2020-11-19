# import pygame library and initialize game engine 
import random 
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

ballCount = 0
ballCoords = []
ballRads = []
ballColors = []

def generateBall():
    ballCoords.append((random.randint(0, 640), random.randint(0, 480))) 
    ballRads.append(random.randint(10, 40))
    ballColors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# ---------- Main Program Loop ----------
while carryOn: 
    # --- Main event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                generateBall()
                ballCount += 1
            if event.key == pygame.K_r:
                ballCount = 0
                ballCoors = []
                ballRads = []
                ballColors = []

    # --- Game logic 

    # --- Drawing onto screen 
    screen.fill(WHITE)
    for i in range(ballCount):
        pygame.draw.circle(screen, ballColors[i], ballCoords[i], ballRads[i])

    # --- Update screen 
    pygame.display.flip() 

    # --- Limit frames per second 
    clock.tick(30)


# after exiting the main program loop, stop the game engine
pygame.quit() 
