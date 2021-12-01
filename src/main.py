from generators.depth_first_search import DepthFirstSearchMG
from generators.maze_generator import MazeGenerator

from typing import List, Tuple, Union
import pygame

# Color Settings
BACKGROUND_COLOR: Tuple[int, int, int] = (248, 248, 248)
WALL_COLOR: Tuple[int, int, int] = (13, 13, 13)
START_COLOR: Tuple[int, int, int] = (0, 248, 0)
END_COLOR: Tuple[int, int, int] = (248, 0, 0)

# Maze Settings
MAZE_SIZE: int = 50 # Maze extents = SIZE * SIZE, Maze will always be square
maze: List[List[bool]] = [ [True] * MAZE_SIZE for _ in range(0, MAZE_SIZE) ]

# PyGame Variables
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


def draw_maze(cell_size: int) -> None:
    global MAZE_SIZE
    global screen
    global maze
    
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
    generator: Union[MazeGenerator, None] = DepthFirstSearchMG(maze=maze)
    
    if generator:
        generator.generate()
    
    while True:
        width, height = screen.get_size()
        screen.fill(BACKGROUND_COLOR)
        
        cell_size: int = ((width + height) // 2) // MAZE_SIZE
        draw_maze(cell_size=cell_size)

        if generator:
            sx, sy = generator.start
            ex, ey = generator.end
            
            sx *= cell_size
            sy *= cell_size
            ex *= cell_size
            ey *= cell_size
            
            start_rect = pygame.Rect(sx, sy, cell_size, cell_size)
            end_rect = pygame.Rect(ex, ey, cell_size, cell_size)
            screen.fill(START_COLOR, start_rect)
            screen.fill(END_COLOR, end_rect)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        pygame.display.flip()


if __name__ == "__main__":
    main()