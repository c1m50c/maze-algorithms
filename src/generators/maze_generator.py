from typing import List, Tuple


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
        
        self.maze = maze
        self.start = (0, 0)
        self.end = (0, 0)
    
    def generate(self) -> None:
        """
            When called the `maze` will mutate into a maze coresponding to the output of the implemented algorithm.
        """
        ...