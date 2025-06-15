from src.maze import Maze

maze = Maze()
maze.load_from_csv("data/example_maze.csv")
maze.display()