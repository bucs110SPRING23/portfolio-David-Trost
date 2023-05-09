import pygame

pygame.init()

screen=pygame.display.set_mode()
screen.fill((255,255,255))
pygame.display.update()

info=pygame.display.Info()
screen_width=info.current_w
screen_height=info.current_h
print("Screen width:", screen_width)
print("Screen height:", screen_height)


pygame.draw.circle(screen, (0,0,255), [768,432], 50,5)
pygame.draw.circle(screen, (0,0,255), [768,557],75,5)
pygame.draw.circle(screen, (0,0,255), [768,727],100,5)

pygame.display.flip()

pygame.time.delay(5000)

