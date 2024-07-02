import pygame

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLUMNS = 4
RECT_WIDTH = WIDTH // COLUMNS
RECT_HEIGHT = HEIGHT // ROWS
OUTLINE_COLOR = (187, 173 , 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192 , 180)
FONT_COLOR = (119, 110 , 101)

pygame.display.set_caption('2048')
FONT = pygame.font.SysFont('comicsans', 60, bold=True)
MOVE_VEL = 20
WINDOW = pygame.display.set_mode((HEIGHT,WIDTH))

def draw_grid(window):
    for row in range(1,ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window,OUTLINE_COLOR, (0,y), (WIDTH,y), OUTLINE_THICKNESS )

    for column in range(1,COLUMNS):
        x = column * RECT_WIDTH
        pygame.draw.line(window,OUTLINE_COLOR,(x,0),(x,HEIGHT),OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0,0,WIDTH,HEIGHT), OUTLINE_THICKNESS)

def draw(window):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window)

    pygame.quit()

if __name__ == '__main__':
    main(WINDOW)