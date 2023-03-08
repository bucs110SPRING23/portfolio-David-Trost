import pygame
pygame.init()

#PARTA
screen= pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_width, screen_height = pygame.display.get_surface().get_size()
screen.fill((3, 144, 252))

white = (255, 255, 255)
black = (0, 0, 0)
red = (252, 3, 78)
blue = (3, 144, 252)
green=(0,255,0)
yellow=(255,255,0)

dartboard_radius = min(screen_width, screen_height) // 2
dartboard_center = (screen_width//2, screen_height//2)
pygame.draw.circle(screen, red, dartboard_center, dartboard_radius, 0)

start_point = (dartboard_center[0] - dartboard_radius, dartboard_center[1])
end_point = (dartboard_center[0] + dartboard_radius, dartboard_center[1])
pygame.draw.line(screen, black, start_point, end_point, 5)
pygame.draw.line(screen, black, (dartboard_center[0], dartboard_center[1] - dartboard_radius), (dartboard_center[0], dartboard_center[1] + dartboard_radius), 5)


#PARTB
import random
import math
for i in range(10):
    x = random.randrange(0, screen_width)
    y = random.randrange(0, screen_height)
    distance_from_center = math.hypot(x-dartboard_center[0], y-dartboard_center[1])
    if distance_from_center <= dartboard_radius:
        color = green
    else:
        color = yellow
    pygame.draw.circle(screen, color, (x, y), 4, 0)

running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    
    # update the screen
    pygame.display.flip()

# quit Pygame
pygame.quit()