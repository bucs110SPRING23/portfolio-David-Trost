import pygame 

# refactored function 
def threenp1(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count = count + 1
    return count

def threenp1range(n, upper_limit):
    objs_in_sequence = {}
    for n in range(2, upper_limit+1):
        iters = threenp1(n)
        objs_in_sequence[n] = iters
    return objs_in_sequence


def main():
    n = 10
    upper_limit = 100
    threenplus1_iters_dict = threenp1range(n, upper_limit)
    print(threenplus1_iters_dict)
    graph_coordinates(threenplus1_iters_dict)

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    font = pygame.font.Font(None, 30)
    factor = 5
    display_size = (100 * factor, max(threenplus1_iters_dict.values()) * factor)
    display = pygame.Surface(display_size)
    display.fill((255, 255, 255))
    coordinates = [(n, iters) for n, iters in threenplus1_iters_dict.items()]
    max_so_far = max(threenplus1_iters_dict.values())
    for i in range(len(coordinates) - 1):
        pygame.draw.line(display, (255, 0, 0), (coordinates[i][0] * factor, display_size[1] - coordinates[i][1] * factor),
                         (coordinates[i+1][0] * factor, display_size[1] - coordinates[i+1][1] * factor), 1)
    new_display = pygame.transform.flip(display, False, True)
    new_display = pygame.transform.scale(new_display, (display_size[0] * factor, display_size[1] * factor))
    screen = pygame.display.set_mode(display_size)
    screen.blit(new_display, (0, 0))
    max_so_far_text = font.render("Max so far: " + str(max_so_far), True, (0, 0, 0))
    screen.blit(max_so_far_text, (10, 10))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()
