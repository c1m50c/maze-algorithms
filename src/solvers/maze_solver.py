from typing import List, Tuple


class MazeSolver:
    """
        Class for solving mazes, ment to be inherited from for implementing various maze solving algorithms.
        
        ## Fields
        ```py
        maze: List[List[bool]] # Maze Matrix, to be read with the implemented algorithm.
        path: List[Tuple[int, int]] # Indicies of the Maze Matrix, coresponding to the solved path.
        start: Tuple[int, int] # Indicies of the Maze representing the start of the Maze.
        end: Tuple[int, int] # Indicies of the Maze representing the end of the Maze.
        ```
    """
    
    maze: List[List[bool]]
    path: List[Tuple[int, int]]
    start: Tuple[int, int]
    end: Tuple[int, int]
    __slots__ = "maze", "path", "start", "end"
    
    def __init__(self, maze: List[List[bool]], start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
            Class for solving mazes, ment to be inherited from for implementing various maze solving algorithms.
            
            ## Paramaters
            ```py
            maze: List[List[bool]] # Maze Matrix, to be read with the implemented algorithm.
            start: Tuple[int, int] # Indicies of the Maze representing the start of the Maze.
            end: Tuple[int, int] # Indicies of the Maze representing the end of the Maze.
            ```
        """
    
        self.maze = maze
        self.path = [  ]
        self.start = start
        self.end = end
    
    def solve(self) -> None:
        """
            When called the `path` will be mutated into a list of matrix indicies representing the output path
            of the solving algorithm.
        """
        ...