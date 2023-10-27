import queue

# maze = [
#         ['#', '#', '#', 'O', '#'],
#         ['#', ' ', ' ', ' ', '#'],
#         ['#', ' ', '#', ' ', '#'],
#         ['#', ' ', ' ', ' ', '#'],
#         ['#', 'X', '#', '#', '#']
#     ]

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
    for char in path:
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

def main():
    q = queue.Queue()
    q.put('')

    start_point = 'O'
    i,j = find_point(maze, start_point)
    while start_point != 'X':
        path = q.get()

        # check that present coordinate is not already
        # been passed through
        #     - if the last element is L, the next one shouldn't
        #     - be R and vice-versa
        #     - if the last element is U, the next one shouldn't
        #     - be D and vice-versa

        for point in ['L', 'R', 'D', 'U']:
            row, col = resolve_path_coordinate(path + point, i, j)
            if (len(maze)-1 >= row >= 0) and (len(maze[0])-1 >= col >= 0):
                char = maze[row][col]
                if char != '#':
                    if char == 'X':
                        start_point = char
                        break
                    q.put(path + point)

    print_maze(maze, 'O', path=path)

if __name__ == "__main__":
    # Ensure that there is a start and end point
    assert find_point(maze, 'O') and find_point(maze, 'X')

    main()

