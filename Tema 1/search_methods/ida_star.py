# Distanta euclidiana
from math import sqrt
def euclidean_distance(a, b):
    return sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]))


# Distanta Manhattan
def manhattan_distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])


# Distanta BFS
from collections import deque
def bfs_distance(x1, y1, x2, y2, obstacles, map_length, map_width):
    visited = set()
    queue = deque()
    queue.append((x1, y1, 0))
    visited.add((x1, y1))

    while queue:
        (current_x, current_y, current_distance) = queue.popleft()

        if (current_x, current_y) == (x2, y2):
            return current_distance
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx = dx + current_x
            ny = dy + current_y

            if (nx, ny) not in visited and (nx, ny) not in obstacles and (0 <= nx < map_length) and (0 <= ny < map_width):
                queue.append((nx, ny, current_distance + 1))
                visited.add((nx, ny))

    return float('inf')


# Asocierea cutie-tinta
from itertools import permutations

def box_target_association_bruteforce(boxes, targets, obstacles, map_length, map_width):
    box_list = list(boxes.items())
    min_total_cost = float('inf')
    best_association = None

    for target_perm in permutations(targets, len(box_list)):
        total_cost = 0
        association = {}

        for (box_name, box), target in zip(box_list, target_perm):
            # cost = euclidean_distance((boxes[box_name].x, boxes[box_name].y), (target[0], target[1]))
            # cost = manhattan_distance((boxes[box_name].x, boxes[box_name].y), (target[0], target[1]))
            cost = bfs_distance(box.x, box.y, target[0], target[1], obstacles, map_length, map_width)
            total_cost += cost
            association[box_name] = target

        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_association = association

    return best_association, min_total_cost


def ida_star(start_node):
    length = start_node.length
    width = start_node.width
    player = start_node.player
    boxes = start_node.boxes
    obstacles = start_node.obstacles
    targets = start_node.targets

    threshold = 0
    box_target_association = {}
    box_target_association, threshold = box_target_association_bruteforce(boxes, targets, obstacles, length, width)

    # NUmarul de pasi
    steps = 0

    # Aproximare initiala a solutiei
    for (box_name, box) in boxes.items():
        # threshold += euclidean_distance((player.x, player.y), (box.x, box.y))
        # threshold += manhattan_distance((player.x, player.y), (box.x, box.y))
        threshold += bfs_distance(player.x, player.y, box.x, box.y, obstacles, length, width)

    while True:
        visited = set()
        (steps, result) = search(start_node, 0, threshold, visited, box_target_association, steps)
        
        if isinstance(result, list):
            return (result, steps)
        
        if(result==float('inf')):
            return (None, steps)
        
        threshold = result  


def search(state, g, threshold, visited, box_target_association, steps):
    length = state.length
    width = state.width
    player = state.player
    boxes = state.boxes
    obstacles = state.obstacles
    targets = state.targets

    # Cautare informata
    steps += 1
    f = g
    for (box_name, target) in box_target_association.items():
        # f += euclidean_distance((player.x, player.y), (boxes[box_name].x, boxes[box_name].y)) + euclidean_distance((boxes[box_name].x, boxes[box_name].y), (target[0], target[1]))
        # f += manhattan_distance((player.x, player.y), (boxes[box_name].x, boxes[box_name].y)) + manhattan_distance((boxes[box_name].x, boxes[box_name].y), (target[0], target[1]))
        f += bfs_distance(player.x, player.y, boxes[box_name].x, boxes[box_name].y, obstacles, length, width) + bfs_distance(target[0], target[1], boxes[box_name].x, boxes[box_name].y, obstacles, length, width)

    if f > threshold:
        return (steps, f)

    # Returnam solutia
    if state.is_solved():
        return (steps, [state])

    # Marcam nodul ca vizitat pe ramura curenta, evitam ciclurile
    state_id = str(state)
    if state_id in visited:
        return (steps, float('inf'))
    visited.add(state_id)

    # Analiza vecinilor
    min_threshold = float('inf')
    for neighbour in state.get_neighbours():
        (steps, result) = search(neighbour, g+1, threshold, visited, box_target_association, steps)

        # Creare drum
        if isinstance(result, list):
            return (steps, [state] + result)

        if result < min_threshold:
            min_threshold = result

    # Nu s-a gasit stare finala in limita stabilita, marim tresh_hold-ul
    visited.remove(state_id)
    return (steps, min_threshold)
    