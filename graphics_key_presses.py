# import pygame library and initialize game engine 
import pygame
pygame.init() 

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

rect = [50, 50, 70, 70]
rectV = 4
rectColors = [
    (176, 44, 161), 
    (144, 44, 176),
    (44, 84, 176),
    (44, 176, 172),
    (44, 176, 55),
    (172, 176, 44),
    (176, 125, 44),
    (176, 59, 44)
    ]
rectColorIndex = 0

# ---------- Main Program Loop ----------
while carryOn: 
    # --- Main event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rectColorIndex += 1
                rectColorIndex %= len(rectColors)

    # --- Game logic 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        rect[0] -= rectV
    if pressed[pygame.K_RIGHT]:
        rect[0] += rectV
    if pressed[pygame.K_UP]:
        rect[1] -= rectV
    if pressed[pygame.K_DOWN]:
        rect[1] += rectV

    # --- Drawing onto screen 
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, rectColors[rectColorIndex], rect)

    # --- Update screen 
    pygame.display.flip() 

    # --- Limit frames per second 
    clock.tick(30)


# after exiting the main program loop, stop the game engine
pygame.quit() 