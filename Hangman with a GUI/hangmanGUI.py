import colorsys
import pygame

# setting display
pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# loading images
images = []
for i in range(7):
    image = pygame.image.load(r'Hangman with a GUI/images/hangman{}.png'.format(i))
    images.append(image)

# game variables
hangman_status = 0

# color
WHITE = (255,255,255)

FPS = 60
clock = pygame.time.Clock()
run = True

# main game loop
while run:
    clock.tick(FPS)

    window.fill(WHITE)
    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
