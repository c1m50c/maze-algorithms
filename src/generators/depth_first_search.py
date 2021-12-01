# TODO: While the algorithm does conform to its rules, it does not at all function properly,
#   this needs to be fixed.

from .maze_generator import MazeGenerator
from typing import List, Tuple, Set
from random import choice


class DepthFirstSearchMG(MazeGenerator):
    def __init__(self, maze: List[List[bool]]) -> None:
        super().__init__(maze)
    
    def generate(self) -> None:
        stack: List[Tuple[int, int]] = [ self.start ]
        visited: Set[Tuple[int, int]] = set()
        visited.add(self.start)
        
        not_visited = lambda p : p not in visited
        
        while stack:
            current: Tuple[int, int] = stack.pop(choice(seq=[-1, 0]))
            neighbors = self.get_neighboring_indicies(position=current)
            nv_neighbors = [ x for x in neighbors if not_visited(x) ]
            
            if nv_neighbors:
                stack.append(current)
                
                nvn = choice(seq=nv_neighbors)
                i, j = choice(seq=[nvn, current])
                self.maze[i][j] = False
                
                stack.append(nvn)
                visited.add(nvn)