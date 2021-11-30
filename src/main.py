from typing import List, Tuple
import pygame

# Color Settings
BACKGROUND_COLOR: Tuple[int, int, int] = (248, 248, 248)
WALL_COLOR: Tuple[int, int, int] = (21, 21, 21)

# Maze Settings
MAZE_SIZE: int = 32 # Maze extents = SIZE * SIZE, Maze will always be square
maze: List[List[bool]] = [ [True] * MAZE_SIZE for _ in range(0, MAZE_SIZE) ]

# PyGame Variables
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def draw_maze(width: int, height: int) -> None:
    global MAZE_SIZE
    global screen
    global maze
    
    cell_size: int = ((width + height) // 2) // MAZE_SIZE
    
    for i in range(0, MAZE_SIZE):
        for j in range(0, MAZE_SIZE):
            if maze[i][j]: # Is Wall
                x, y = i * cell_size, j * cell_size
                rect = pygame.Rect(x, y, cell_size, cell_size)
                screen.fill(WALL_COLOR, rect)


def main() -> None:
    global screen
    global clock
    global maze
    
    pygame.display.set_caption("Maze Algorithms")
    
    while True:
        width, height = screen.get_size()
        screen.fill(BACKGROUND_COLOR)
        
        draw_maze(width=width, height=height)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        pygame.display.flip()


if __name__ == "__main__":
    main()