import heapq

def correctly_placed_tiles(state, goal_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == goal_state[i][j]:
                count += 1
    return count

def find_tile(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return (i, j)

def swap_tiles(state, pos1, pos2):
    new_state = [list(row) for row in state]
    new_state[pos1[0]][pos1[1]], new_state[pos2[0]][pos2[1]] = new_state[pos2[0]][pos2[1]], new_state[pos1[0]][pos1[1]]
    return new_state

def possible_actions(state):
    actions = []
    zero_pos = find_tile(state, 0)
    i, j = zero_pos
    if i > 0:
        actions.append(('Up', (i - 1, j)))
    if i < 2:
        actions.append(('Down', (i + 1, j)))
    if j > 0:
        actions.append(('Left', (i, j - 1)))
    if j < 2:
        actions.append(('Right', (i, j + 1)))
    return actions

def solve_eight_puzzle(initial_state, goal_state):
    heap = []
    visited = set()
    heapq.heappush(heap, (correctly_placed_tiles(initial_state, goal_state), initial_state))

    while heap:
        _, current_state = heapq.heappop(heap)
        if current_state == goal_state:
            return True

        visited.add(tuple(map(tuple, current_state)))

        for action, new_pos in possible_actions(current_state):
            new_state = swap_tiles(current_state, find_tile(current_state, 0), new_pos)
            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(heap, (correctly_placed_tiles(new_state, goal_state), new_state))
                visited.add(tuple(map(tuple, new_state)))

    return False

iinitial_state=[[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goal_state=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]
result = solve_eight_puzzle(initial_state, goal_state)

if result:
    print("Goal state reached")
    print("Sequence of actions followed is as follows: ",actions)
    print("Goal state reached is as follows: ",goal_state)
else:
    print("No solution found")
