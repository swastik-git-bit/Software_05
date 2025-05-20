from collections import deque

def min_moves_to_collect_all_artifacts(grid):
    rows, cols = len(grid), len(grid[0])
    total_keys = 0
    start_x = start_y = 0

    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell == '@':
                start_x, start_y = i, j
            elif 'a' <= cell <= 'g':
                total_keys |= (1 << (ord(cell) - ord('a')))
    
    queue = deque()
    visited = set()
    
    queue.append((start_x, start_y, 0, 0))  # x, y, keys, steps
    visited.add((start_x, start_y, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, keys, steps = queue.popleft()

        if keys == total_keys:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                cell = grid[nx][ny]
                new_keys = keys

                if cell == '#':
                    continue  

                if 'a' <= cell <= 'g':
                    new_keys |= (1 << (ord(cell) - ord('a')))  

                if 'A' <= cell <= 'G':
                    if not (keys & (1 << (ord(cell) - ord('A')))):
                        continue 

                if (nx, ny, new_keys) not in visited:
                    visited.add((nx, ny, new_keys))
                    queue.append((nx, ny, new_keys, steps + 1))

    return -1  
