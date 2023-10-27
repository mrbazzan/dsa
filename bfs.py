import queue


# def maze():
#     return [
#         ['#', '#', '#', 'O', '#'],
#         ['#', ' ', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', '#'],
#         ['#', ' ', ' ', ' ', '#'],
#         ['#', 'X', '#', '#', '#']
#     ]

# def maze2():
#     return [
#         ['#', '#', '#', '#', 'O', '#'],
#         ['#', ' ', ' ', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', ' ', '#'],
#         ['#', ' ', '#', '#', ' ', '#'],
#         ['#', ' ', ' ', ' ', ' ', '#'],
#         ['#', '#', '#', 'X', '#', '#']]

maze = [
        ['#', '#', '#', '#', 'O', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', 'X', '#', '#']]


def find_point(maze, point):
    for i, line in enumerate(maze):
        if point in line:
            return i, line.index(point)

    raise Exception(f"'{point}' not in maze")


def update_coordinate(char, i, j):
    if char == 'L':
        j = j - 1
    elif char == 'R':
        j = j + 1
    elif char == 'U':
        i = i - 1
    elif char == 'D':
        i = i + 1
    return i, j


def print_maze(maze, point, path=''):
    i, j = find_point(maze, point)

    # `path` includes even the character that matches the
    # endpoint('X'), so there is a need to skip it.
    for char in path[:-1]:
        i, j = update_coordinate(char, i, j)
        maze[i][j] = '+'

    print('\n'.join([' '.join(line) for line in maze]))


def resolve_path_coordinate(x, i, j):
    """
    Given a path, return the new coordinate after resolving

    x - the path. e.g 'LLDD'
    """
    for char in x:
        i, j = update_coordinate(char, i, j)
    return i, j


# Ensure that there is a start and end point
assert find_point(maze, 'O') and find_point(maze, 'X')

q = queue.Queue()
q.put('')

height = len(maze)
width = len(maze[0])

start = 'O'
i,j = find_point(maze, start)
while start != 'X':

    x = q.get()

    # check that present coordinate is not already
    # been passed through
    #     - if the last element is L, the next one shouldn't
    #     - be R and vice-versa
    #     - if the last element is U, the next one shouldn't
    #     - be D and vice-versa

    # LEFT
    a, b = resolve_path_coordinate(x + 'L', i, j)
    if b >= 0 and b <= width - 1:
        if maze[a][b] != '#':
            q.put(x + 'L')

    # RIGHT
    a, b = resolve_path_coordinate(x + 'R', i, j)
    if b >= 0 and b <= width - 1:
        if maze[a][b] != '#':
            q.put(x + 'R')

  # DOWN
    a, b = resolve_path_coordinate(x + 'D', i, j)
    if a >= 0 and a <= height - 1:    
        if maze[a][b] != '#':
            q.put(x + 'D')

    # UP
    a, b = resolve_path_coordinate(x + 'U', i, j)
    if a >= 0 and a <= height - 1:
        if maze[a][b] != '#':
            q.put(x + 'U')

    first, second = resolve_path_coordinate(x, i, j)
    start = maze[first][second]


print_maze(maze, 'O', path=x)

