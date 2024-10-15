# Lucky Khounvongsa, 20172476
# Salim Fathya, 20210127

import sys
import random

# Dimensions du labyrinte
cell_size = 10  # mm
wall_height = 10  # mm
wall_thickness = 1  # mm
floor_thickness = 1  # mm

sizex = 10
sizey = 10

class Strategy:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.walls = [[[1, 1, 1, 1] for _ in range(size_x)] for _ in range(size_y)]
        self.visited = [[0 for _ in range(size_x)] for _ in range(size_y)]
    
    def Apply(self):
        pass

class Algorithm1(Strategy):
    def __init__(self, size_x, size_y):
        super().__init__(size_x, size_y)
        self.maze = MazeDFS(size_x, size_y)

    def Apply(self):
        print("Applying Dept-First Search (DFS)")
        print("Applying Algorithm1")
        self.maze.generate()
        return self.maze.walls  

class Algorithm2(Strategy):
    def __init__(self, size_x, size_y):
        super().__init__(size_x, size_y)
        self.maze = MazeKruskal(size_x, size_y)

    def Apply(self):
        print("Applying Kruskal")
        print("Applying Algorithm2")
        self.maze.generate()
        return self.maze.walls

class Generator:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def SetStrategy(self, strategy):
        self.strategy = strategy

    def Generate(self):
        return self.strategy.Apply()

class Creator:
    def __init__(self, algorithm_name, filename="labyrinthe_{}.scad"):
        self.filename = filename.format(algorithm_name)

    def PrintLabyrinth(self, walls):
        global sizex, sizey, cell_size, wall_height, wall_thickness, floor_thickness
        total_length_x = cell_size * len(walls[0]) 
        total_length_y = cell_size * len(walls)   

        with open(self.filename, 'w') as f:
            f.write("difference() {\n")
            f.write("union() {\n")
            # Ajout du plancher sous le labyrinthe
            f.write(f"translate([{-wall_thickness / 2}, {-wall_thickness / 2}, -{floor_thickness}]) ")
            f.write(f"cube([{total_length_x + wall_thickness}, {total_length_y + wall_thickness}, {floor_thickness}]);\n")

            for y in range(sizey):
                for x in range(sizex):
                    cell_walls = walls[y][x]
                    # Génère les murs intérieurs du labyrinthe
                    # Mur gauche
                    if x > 0 and cell_walls[0]:  
                        f.write(f"translate([{x * cell_size - wall_thickness / 2}, {y * cell_size}, 0]) cube([{wall_thickness}, {cell_size}, {wall_height}]);\n")
                    # Mur Supérieur
                    if y < sizey - 1 and cell_walls[1]:  
                        f.write(f"translate([{x * cell_size}, {(y + 1) * cell_size - wall_thickness / 2}, 0]) cube([{cell_size}, {wall_thickness}, {wall_height}]);\n")
                    # Mur Droite
                    if x < sizex - 1 and cell_walls[2]:  
                        f.write(f"translate([{(x + 1) * cell_size - wall_thickness / 2}, {y * cell_size}, 0]) cube([{wall_thickness}, {cell_size}, {wall_height}]);\n")
                    # Mur Inférieur
                    if y > 0 and cell_walls[3]: 
                        f.write(f"translate([{x * cell_size}, {y * cell_size - wall_thickness / 2}, 0]) cube([{cell_size}, {wall_thickness}, {wall_height}]);\n")

            # Génère les murs externes du labyrinte
            # Mur Gauche
            for y in range(sizey):
                f.write(f"translate([{-wall_thickness / 2}, {y * cell_size}, 0]) cube([{wall_thickness}, {cell_size}, {wall_height}]);\n")
            # Mur Suppérieur
            for x in range(sizex):
                f.write(f"translate([{x * cell_size}, {total_length_y - wall_thickness / 2}, 0]) cube([{cell_size}, {wall_thickness}, {wall_height}]);\n")
            # Mur Droite
            for y in range(sizey):
                f.write(f"translate([{total_length_x - wall_thickness / 2}, {y * cell_size}, 0]) cube([{wall_thickness}, {cell_size}, {wall_height}]);\n")
            # Mur Inférieur
            for x in range(sizex - 1):
                f.write(f"translate([{x * cell_size}, {-wall_thickness / 2}, 0]) cube([{cell_size}, {wall_thickness}, {wall_height}]);\n")

            # Ajout du logo
            f.write("// logo\n")
            f.write("color([0, 1, 0, 1]){\n")
            f.write("translate([1, -0.2, 1]){\n")
            f.write("rotate([90, 0, 0]){\n")
            f.write("linear_extrude(1)\n")
            f.write('text("IFT2125 LK et SF", size=7.0);\n')
            f.write("}\n")
            f.write("}\n")
            f.write("}\n")  

            f.write("}\n") 
            f.write("}\n") 


# Labyrinthe fait à l'aide de DFS
class MazeDFS(Strategy):
    def is_full(self):
        return all(all(row) for row in self.visited)

    def generate(self):
        stack = []
        x, y = 0, 0
        self.visited[y][x] = 1
        stack.append((x, y))
        while not self.is_full():
            neighbors = self.find_neighbors(x, y)
            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)
                self.remove_wall(x, y, dx, dy)
                x, y = nx, ny
                self.visited[ny][nx] = 1
                stack.append((nx, ny))
            else:
                x, y = stack.pop()

    def find_neighbors(self, x, y):
        directions = [(x-1, y, 0), (x, y+1, 1), (x+1, y, 2), (x, y-1, 3)]
        valid = []
        for nx, ny, idx in directions:
            if 0 <= nx < self.size_x and 0 <= ny < self.size_y and not self.visited[ny][nx]:
                valid.append((nx, ny, idx, (idx + 2) % 4))  
        return valid

    def remove_wall(self, x, y, idx, opposite_idx):
        self.walls[y][x][idx] = 0
        nx, ny = x + (idx == 2) - (idx == 0), y + (idx == 1) - (idx == 3)
        self.walls[ny][nx][opposite_idx] = 0


# Labyrinthe fait à l'aide de Kruskal
class MazeKruskal(Strategy):
    def generate(self):
        walls = []
        for y in range(self.size_y):
            for x in range(self.size_x):
                if x > 0:
                    walls.append(((x, y), (x - 1, y)))
                if y > 0:
                    walls.append(((x, y), (x, y - 1)))

        random.shuffle(walls)
        sets = {i: {i} for i in range(self.size_x * self.size_y)}

        def find_set(v):
            for s, items in sets.items():
                if v in items:
                    return s
            return None

        for (x1, y1), (x2, y2) in walls:
            set1 = find_set(y1 * self.size_x + x1)
            set2 = find_set(y2 * self.size_x + x2)
            if set1 is not None and set2 is not None and set1 != set2:
                self.remove_wall(x1, y1, x2, y2)
                sets[set1] |= sets[set2]
                del sets[set2]

    def remove_wall(self, x1, y1, x2, y2):
        if x1 == x2:
            if y1 < y2:
                self.walls[y1][x1][1] = 0
                self.walls[y2][x2][3] = 0
            else:
                self.walls[y1][x1][3] = 0
                self.walls[y2][x2][1] = 0
        elif y1 == y2:
            if x1 < x2:
                self.walls[y1][x1][2] = 0
                self.walls[y2][x2][0] = 0
            else:
                self.walls[y1][x1][0] = 0
                self.walls[y2][x2][2] = 0


def main():
    global strategy_choice
    args = sys.argv[:]
    if len(args) >= 2:
        strategy_choice = int(args[1])
    else:
        strategy_choice = 1 

    global algorithm_name
    algorithm_name = "algo1" if strategy_choice == 1 else "algo2"

    my_generator = Generator()
    if strategy_choice == 1:
        my_generator.SetStrategy(Algorithm1(sizex, sizey))  
    elif strategy_choice == 2:
        my_generator.SetStrategy(Algorithm2(sizex, sizey))  
    else:
        print("Error: Strategy choice")
        return

    walls = my_generator.Generate()

    my_creator = Creator(algorithm_name)
    my_creator.PrintLabyrinth(walls)

if __name__ == "__main__":
    main()