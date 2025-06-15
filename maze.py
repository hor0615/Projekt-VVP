import numpy as np
import matplotlib.pyplot as plt

class Maze:
    def __init__(self):
        self.grid = None
    def load_from_csv(self, path: str):
        try:
            raw = np.loadtxt(path, delimiter=',', dtype=int)
            self.grid = raw.astype(bool)
        except Exception as e:
            print(f"Error loading labyrinth: {e}")
            self.grid = None
    def display(self):
        if self.grid is None:
            print("Labyrint not loaded.")
            return
        for row in self.grid:
            print("".join("#" if cell else " " for cell in row))
    def plot_path(self, path):
            if self.grid is None:
                print("Labyrinth not loaded")
                return

            fig, ax = plt.subplots()
            ax.imshow(self.grid, cmap="gray_r")

            if path:
                y_coords, x_coords = zip(*path)
                ax.plot(x_coords, y_coords, color="red", linewidth=2, marker='o')

            plt.title("Labyrinth with path found")
            plt.axis("off")
            plt.show()
    def save_path(self, path, filename="output_path.csv"):
        import csv
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["row", "col"])
            for r, c in path:
                writer.writerow([r, c])
