from collections import deque

def path_finder(maze):
    maze = [list(row) for row in maze.split('\n')]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    n = len(maze)

    visited = set()
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, steps = queue.popleft()

        if x == n - 1 and y == n - 1:
            return steps

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and maze[nx][ny] == '.':
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return False
