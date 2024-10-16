possibilities = ["de volta a cabana.", "encontrou o fim da floresta.", "andou em circulos.", "caminho sem saida."]

moves_test = [
  ["S", "S", "O", "S"],
  ["O", "C", "L", "S"],
  ["S", "S", "N", "O"],
  ["O", "L", "L", "F"]
]

# ↑, ↓, →, ←
# N, S, L, O
# C representa a cabana; F o fim da floresta;

def simulate(matrix, direction, new_x, new_y, pivot_x, pivot_y):
    visited_indexes = set()
    x, y = new_x, new_y
    
    while True:
        if (x, y) in visited_indexes:
            if x == pivot_x and y == pivot_y:
                print(f"{direction}: {possibilities[0]}")
                return
            else:
                print(f"{direction}: {possibilities[2]}")
                return

        visited_indexes.add((x, y))

        new_direction = matrix[x][y]
        if new_direction == "F":
            print(f"{direction}: {possibilities[1]}")
            return

        x, y = move(matrix, x, y, new_direction)
        if x is None or y is None:
            print(f"{direction}: {possibilities[3]}")
            return

def move(matrix, pivot_x, pivot_y, direction):
    dx, dy = 0, 0
    if direction == "N":
        dx, dy = -1, 0
    elif direction == "S":
        dx, dy = 1, 0 
    elif direction == "L":
        dx, dy = 0, 1 
    elif direction == "O":
        dx, dy = 0, -1
    
    new_x, new_y = pivot_x + dx, pivot_y + dy

    max_axis_y = len(matrix[0])
    max_axis_x = len(matrix)

    if 0 <= new_x < max_axis_x and 0 <= new_y < max_axis_y:
        return new_x, new_y
    else:
        return None, None
    

def generate_matrix(x, y, moves):
    pivot_x = None
    pivot_y = None
    matrix = []
    for i in range(x):
        lines = []
        for j in range(y):
            if moves[i][j] == "C":
                pivot_x, pivot_y = i, j

            lines.append(moves[i][j])

        matrix.append(lines)

    return (matrix, pivot_x, pivot_y)

def init():
    x = None
    y = None
    matrix = []

    while True:
        if not x and not y:
            x, y = input().split(' ')

        moves = input().split(' ')
        matrix.append([move for move in moves])

        if len(matrix) == int(x):
            matrix, pivot_x, pivot_y = generate_matrix(int(x), int(y), matrix)
            for direction in ["N", "S", "L", "O"]:
                new_x, new_y = move(matrix, pivot_x, pivot_y, direction)
                if new_x is not None and new_y is not None:
                    simulate(matrix, direction, new_x, new_y, pivot_x, pivot_y)
                else:
                    print(f"{direction}: {possibilities[3]}")

            return
init()

# def test():
#     matrix, pivot_x, pivot_y = generate_matrix(4, 4, moves_test)
#     for direction in ["N", "S", "L", "O"]:
#         new_x, new_y = move(matrix, pivot_x, pivot_y, direction)
#         if new_x is not None and new_y is not None:
#             simulate(matrix, direction, new_x, new_y, pivot_x, pivot_y)
#         else:
#             print(f"{direction}: {possibilities[3]}")

# test()