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
        
        n: int = len(maze) - 1
        
        self.maze = maze
        self.start = (0, 0)
        self.end = (n, n)
    
    def generate(self) -> None:
        """
            When called the `maze` will mutate into a maze coresponding to the output of the implemented algorithm.
        """
        ...
    
    def get_neighboring_indicies(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
            Returns a list containing the indicies of neighboring cells at the given `position`.
            
            ## Parameters
            ```py
            position: Tuple[int, int] # Position of Cell to get neighbors from.
            ```
        """
        
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

    def get_neighboring_walls(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
            Returns a list of indicies of neighboring wall cells.
            
            ## Parameters
            ```py
            position: Tuple[int, int] # Position of the cell to retrieve neighboring wall cells.
            ```
        """
        
        return [ x for x in self.get_neighboring_indicies(position=position) if self.maze[x[0]][x[1]] ]
    
    def get_neighboring_empty(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
            Returns a list of indicies of neighboring empty cells.
            
            ## Parameters
            ```py
            position: Tuple[int, int] # Position of the cell to retrieve neighboring empty cells.
            ```
        """
        
        return [ x for x in self.get_neighboring_indicies(position=position) if not self.maze[x[0]][x[1]] ]
    
    @staticmethod
    def in_bounds(position: Tuple[int, int], size: int) -> bool:
        """
            Returns `True` if the given `position` is within the maze matrix.

            ## Parameters
            ```py
            position: Tuple[int, int] # Position of the Cell to check.
            size: int # Maximum index of the maze matrix.
            ```
        """
        
        x, y = position
        if x < 0 or x > size: return False
        if y < 0 or y > size: return False
        return True