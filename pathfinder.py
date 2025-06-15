from collections import deque

class Pathfinder:
    def __init__(self, maze):
        self.maze = maze.grid
        self.rows, self.cols = self.maze.shape

    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_passable(self, r, c):
        return not self.maze[r][c]

    def find_path(self, start, goal):
        queue = deque()
        queue.append((start, [start]))

        visited = set()
        visited.add(start)

        while queue:
            (r, c), path = queue.popleft()

            if (r, c) == goal:
                return path

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc) and self.is_passable(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

        return None
