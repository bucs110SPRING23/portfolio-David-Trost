import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dart Game")
screen_width, screen_height = pygame.display.get_surface().get_size()

white = (255, 255, 255)
black = (0, 0, 0)
red = (252, 3, 78)
blue = (3, 144, 252)
green = (0, 255, 0)
yellow = (255, 255, 0)

dartboard_radius = min(screen_width, screen_height) // 2
dartboard_center = (screen_width // 2, screen_height // 2)
pygame.draw.circle(screen, white, dartboard_center, dartboard_radius, 0)

start_point = (dartboard_center[0] - dartboard_radius, dartboard_center[1])
end_point = (dartboard_center[0] + dartboard_radius, dartboard_center[1])
pygame.draw.line(screen, black, start_point, end_point, 5)
pygame.draw.line(screen, black, (dartboard_center[0], dartboard_center[1] - dartboard_radius), (dartboard_center[0], dartboard_center[1] + dartboard_radius), 5)

player1_box = pygame.Rect(50, 200, 50, 50)
pygame.draw.rect(screen, red, player1_box)
player2_box = pygame.Rect(700, 200, 50, 50)
pygame.draw.rect(screen, blue, player2_box)

pygame.display.flip()

player_selected = False
while not player_selected:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if player1_box.collidepoint(mouse_pos):
                user_selection = "player1"
                player_selected = True
            elif player2_box.collidepoint(mouse_pos):
                user_selection = "player2"
                player_selected = True

player_colors = [red, blue]
player_names = ['Red', 'Blue']
player_scores = [0, 0]

for round_num in range(1, 11):
    player_index = round_num % 2
    player_color = player_colors[player_index]
    player_name = player_names[player_index]

    dart_x = random.randrange(dartboard_center[0] - dartboard_radius, dartboard_center[0] + dartboard_radius)
    dart_y = random.randrange(dartboard_center[1] - dartboard_radius, dartboard_center[1] + dartboard_radius)

    distance_from_center = math.hypot(dart_x - dartboard_center[0], dart_y - dartboard_center[1])

    if distance_from_center <= dartboard_radius:
        color = player_color
        hit_text = f"{player_name} hit!"
        player_scores[player_index] += 1
    else:
        color = yellow
        hit_text = f"{player_name} missed."

    dart_on_board_x = dart_x - dartboard_center[0] + screen_width // 2
    dart_on_board_y = dart_y - dartboard_center[1] + screen_height // 2
    pygame.draw.circle(screen, color, (dart_on_board_x, dart_on_board_y), 4, 0)
    pygame.display.flip()
    pygame.time.wait(500)  # Wait for a short duration between each dart throw

if player_scores[0] > player_scores[1]:
    winner = player_names[0]
elif player_scores[1] > player_scores[0]:
    winner = player_names[1]
else:
    winner = "Tie"

font = pygame.font.SysFont(None, 60)
if winner == "Tie":
    text = font.render("Tie", True, green)
else:
    text = font.render(f"{winner} wins", True, green)

x = screen_width // 2 - text.get_width() // 2
y = screen_height // 2 - text.get_height() // 2
screen.blit(text, (x, y))

if user_selection == "player1":
    if winner == "Red":
        outcome_text = "Congrats, you predicted the right outcome!"
    else:
        outcome_text = "Sorry, you predicted the wrong outcome."
elif user_selection == "player2":
    if winner == "Blue":
        outcome_text = "Congrats, you predicted the right outcome!"
    else:
        outcome_text = "Sorry, you predicted the wrong outcome."

font = pygame.font.SysFont(None, 50)
outcome_message = font.render(outcome_text, True, green)

x = screen_width // 2 - outcome_message.get_width() // 2
y = screen_height // 2 + text.get_height() // 2 + 20
screen.blit(outcome_message, (x, y))
pygame.display.flip()
pygame.time.wait(5000)

pygame.quit()




