from collections import deque
from math import sqrt

def euclidian_distance(a, b):
    return sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]))


def manhattan_distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])


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


# Costul pentru fiecare stare - Euclidian
def euclidian_heuristic_for_state(state, current_box_name, box_target_association):
    player = state.player
    boxes = state.boxes
    obstacles = state.obstacles
    targets = state.targets

    box = boxes[current_box_name]
    target = box_target_association[current_box_name]

    return euclidian_distance((box.x, box.y), target) + euclidian_distance((player.x, player.y), (box.x, box.y))


# Costul pentru fiecare stare - Manhattan
def manhattan_heuristic_for_state(state, current_box_name, box_target_association):
    player = state.player
    boxes = state.boxes
    obstacles = state.obstacles
    targets = state.targets

    box = boxes[current_box_name]
    target = box_target_association[current_box_name]

    return manhattan_distance((box.x, box.y), target) + manhattan_distance((player.x, player.y), (box.x, box.y))


# Costul pentru fiecare stare - BFS
def bfs_heuristic_for_state(state, current_box_name, box_target_association):
    player = state.player
    boxes = state.boxes
    obstacles = state.obstacles
    targets = state.targets
    length = state.length
    width = state.width


    box = boxes[current_box_name]
    target = box_target_association[current_box_name]

    return bfs_distance(box.x, box.y, target[0], target[1], obstacles, length, width) + bfs_distance(player.x, player.y, box.x, box.y, obstacles, length, width)


from collections import deque

def beam_search(start_node, beam_width):
    player = start_node.player
    boxes = start_node.boxes
    obstacles = start_node.obstacles
    targets = start_node.targets
    length = start_node.length
    width = start_node.width

    # Asociere cutie-tinta
    box_target_association = {}
    assigned_targets = set()

    for (box_name, box) in boxes.items():
        min_box_target = float('inf')
        set_target = None

        for target in targets:
            #if manhattan_distance((target[0], target[1]), (box.x, box.y)) < min_box_target and target not in assigned_targets:
            #    min_box_target = manhattan_distance((target[0], target[1]), (box.x, box.y))
            #if euclidian_distance((target[0], target[1]), (box.x, box.y)) < min_box_target and target not in assigned_targets:
            #    min_box_target = euclidian_distance((target[0], target[1]), (box.x, box.y))
            if bfs_distance(target[0], target[1], boxes[box_name].x, boxes[box_name].y, obstacles, length, width) < min_box_target and target not in assigned_targets:
                min_box_target = bfs_distance(target[0], target[1], boxes[box_name].x, boxes[box_name].y, obstacles, length, width)
                set_target = target

        box_target_association[box_name] = set_target
        assigned_targets.add(set_target)


    # BFS pe arborele de stari
    remaining_boxes = list(box_target_association.keys())

    queue = deque([(start_node, [])])
    visited = set()
    visited.add(str(start_node))

    steps = 0

    while queue:
        steps += 1
        (current_node, current_path) = queue.popleft()

        if current_node.is_solved():
            return (steps, current_path)

        # Lista tuturor vecinilor, ii marcam ca vizitati
        selected_nodes = []
        for neigh in current_node.get_neighbours():
            if(str(neigh) not in visited):
                selected_nodes.append((neigh, current_path + [neigh]))
                visited.add(str(neigh))

        # Alegem cele mai bune beam_width stari
        if remaining_boxes:
            #selected_nodes.sort(key=lambda item: manhattan_heuristic_for_state(item[0], remaining_boxes[0], box_target_association))
            #selected_nodes.sort(key=lambda item: euclidian_heuristic_for_state(item[0], remaining_boxes[0], box_target_association))
            selected_nodes.sort(key=lambda item: bfs_heuristic_for_state(item[0], remaining_boxes[0], box_target_association))


        selected_nodes = selected_nodes[:beam_width]
        queue += selected_nodes

        # Eliminam cutia deja plasata pe pozitie
        if remaining_boxes:
            current_box_obj = current_node.boxes[remaining_boxes[0]]
            target = box_target_association[remaining_boxes[0]]
            if (current_box_obj.x, current_box_obj.y) == target:
                remaining_boxes.pop(0)

    return (steps, None)