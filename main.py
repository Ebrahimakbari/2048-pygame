import pygame

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLUMNS = 4
RECT_HEIGHT = WIDTH // COLUMNS
RECT_HEIGHT = HEIGHT // ROWS
OUTLINE_COLOR = (187, 173 , 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192 , 180)
FONT_COLOR = (119, 110 , 101)

pygame.display.set_caption('2048')
FONT = pygame.font.SysFont('comicsans', 60, bold=True)
MOVE_VEL = 20
WINDOW = pygame.display.set_mode((HEIGHT,WIDTH))

def main(window):
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == '__main__':
    main(WINDOW)