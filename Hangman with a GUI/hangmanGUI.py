from math import sqrt
import pygame

# setting display
pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 25)

# loading images
images = []
for i in range(7):
    image = pygame.image.load(
        r'Hangman with a GUI/images/hangman{}.png'.format(i))
    images.append(image)

# game variables
hangman_status = 0

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    window.fill(WHITE)

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()


# main game loop
while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = sqrt((x - m_x)**2 + (y - m_y)**2)
                    if distance < RADIUS:
                        letter[3] = False

pygame.quit()
