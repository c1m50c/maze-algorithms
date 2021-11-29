from typing import List


class MazeGenerator:
    """
        Class for generating mazes, ment to be inherited from for implementing various maze generation algorithms.
        
        ## Fields
        ```py
        maze: List[List[bool]] # Maze Matrix, to be mutated based on the implemented algorithm.
        ```
    """
    
    maze: List[List[bool]]
    __slots__ = "maze"
    
    def __init__(self, maze: List[List[bool]]) -> None:
        """
            Class for generating mazes, ment to be inherited from for implementing various maze generation algorithms.
            
            ## Parameters
            ```py
            maze: List[List[bool]] # Maze Matrix, to be mutated based on the implemented algorithm.
            ```
        """
        
        self.maze = maze
    
    def generate(self) -> None:
        """
            When called the `maze` will mutate into a maze coresponding to the output of the implemented algorithm.
        """
        ...