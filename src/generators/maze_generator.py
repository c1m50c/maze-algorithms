from typing import List, Tuple
from random import randrange


class MazeGenerator:
    """
        Class for generating mazes, ment to be inherited from for implementing various maze generation algorithms.
        
        ## Fields
        ```py
        maze: List[List[bool]] # Maze Matrix, to be mutated based on the implemented algorithm.
        start: Tuple[int, int] # Indicies of the Maze representing the start of the Maze.
        end: Tuple[int, int] # Indicies of the Maze representing the end of the Maze.
        ```
    """
    
    maze: List[List[bool]]
    start: Tuple[int, int]
    end: Tuple[int, int]
    __slots__ = "maze", "start", "end"
    
    def __init__(self, maze: List[List[bool]]) -> None:
        """
            Class for generating mazes, ment to be inherited from for implementing various maze generation algorithms.
            
            ## Parameters
            ```py
            maze: List[List[bool]] # Maze Matrix, to be mutated based on the implemented algorithm.
            ```
        """
        
        n: int = len(maze) - 1
        
        self.maze = maze
        self.start = (randrange(0, n), 0)
        self.end = (randrange(0, n), n)
    
    def generate(self) -> None:
        """
            When called the `maze` will mutate into a maze coresponding to the output of the implemented algorithm.
        """
        ...
    
    def get_neighboring_indicies(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        result: List[Tuple[int, int]] = [  ]
        n: int = len(self.maze) - 1
        i, j = position
        
        if MazeGenerator.in_bounds((i + 1, j), n):
            result.append((i + 1, j))
        if MazeGenerator.in_bounds((i - 1, j), n):
            result.append((i - 1, j))
        if MazeGenerator.in_bounds((i, j + 1), n):
            result.append((i, j + 1))
        if MazeGenerator.in_bounds((i, j - 1), n):
            result.append((i, j - 1))
        
        return result
    
    @staticmethod
    def in_bounds(position: Tuple[int, int], size: int) -> bool:
        x, y = position
        if x < 0 or x > size: return False
        if y < 0 or y > size: return False
        return True