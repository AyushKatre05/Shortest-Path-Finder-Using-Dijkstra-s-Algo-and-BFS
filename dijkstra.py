import pygame
import sys
from tkinter import messagebox, Tk

# Initialize Pygame
pygame.init()

window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width, window_height))

columns = 25
rows = 25

box_width = window_width // columns
box_height = window_height // rows

grid = []
path = []

start_box = None
target_box = None
begin_search = False

class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.wall = False
        self.target = False
        self.start = False
        self.distance = float('inf')
        self.visited = False
        self.neighbours = []
        self.prior = None

    def draw(self, win, color):
        pygame.draw.rect(
            win,
            color,
            (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2),
        )

    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])


# create grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)


# set neighbours
for i in range(columns):
    for j in range(rows):
        grid[i][j].set_neighbours()


def dijkstra():
    global start_box, target_box, begin_search, path
    begin_search = True
    path = []

    start_box.distance = 0
    unvisited = [box for row in grid for box in row]
    while unvisited:
        current_box = min(unvisited, key=lambda box: box.distance)
        unvisited.remove(current_box)
        current_box.visited = True

        for neighbour in current_box.neighbours:
            if not neighbour.wall and not neighbour.visited:
                new_distance = current_box.distance + 1  # Assuming all edges have weight 1
                if new_distance < neighbour.distance:
                    neighbour.distance = new_distance
                    neighbour.prior = current_box

    # Construct path
    current_box = target_box
    while current_box.prior:
        path.append(current_box.prior)
        current_box = current_box.prior


def main():
    global start_box, target_box, begin_search
    while True:
        for event in pygame.event.get():
            # Quit window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # mouse controls
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                # draw wall (only if target hasn't been set yet)
                if event.buttons[0] and not begin_search:
                    i = x // box_width
                    j = y // box_height
                    grid[i][j].wall = True

            # set start point
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and not begin_search:
                i = pygame.mouse.get_pos()[0] // box_width
                j = pygame.mouse.get_pos()[1] // box_height
                if not start_box and not grid[i][j].target:
                    start_box = grid[i][j]
                    start_box.start = True
                else:
                    messagebox.showinfo("Invalid Operation", "Start point already set or overlapping with target.")

            # set target point
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t and not begin_search:
                i = pygame.mouse.get_pos()[0] // box_width
                j = pygame.mouse.get_pos()[1] // box_height
                if not target_box and not grid[i][j].start:
                    target_box = grid[i][j]
                    target_box.target = True
                else:
                    messagebox.showinfo("Invalid Operation", "Target point already set or overlapping with start.")

            # Start algorithm when button is clicked
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and not begin_search:
                if start_box and target_box:
                    dijkstra()
                else:
                    messagebox.showinfo("Missing Points", "Please set both start and target points.")

        window.fill((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                color = (50, 50, 50)
                if box.wall:
                    color = (90, 90, 90)
                elif box.visited:
                    color = (0, 200, 0)
                elif box.start:
                    color = (0, 200, 200)
                elif box.target:
                    color = (200, 200, 0)
                box.draw(window, color)

        # Draw path
        for box in path:
            box.draw(window, (0, 0, 200))

        pygame.display.flip()


main()
