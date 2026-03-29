from queue import PriorityQueue

graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1, 'L': 10, 'M': 2},
    'D': {}, 'E': {},
    'F': {}, 'G': {},
    'J': {}, 'K': {},
    'L': {}, 'M': {}
}
def beam_search(start, goal, beam_width):

    beam = [(0, [start])]

    while beam:

        pq = PriorityQueue()   # fresh pq each round

        for cost, path in beam:
            current_node = path[-1]

            if current_node == goal:
                print(f"Path Found : {' → '.join(path)}")
                print(f"Total Cost : {cost}")
                return

            for neighbor, edge_cost in graph.get(current_node, {}).items():
                new_cost = cost + edge_cost
                if neighbor not in path:
                    new_path = path + [neighbor]
                    pq.put((new_cost, new_path))   # directly into pq ✅

        if pq.empty():
            print("Goal not found")
            return

        # get beam_width smallest directly from pq
        beam = []
        for i in range(min(beam_width, pq.qsize())):
            beam.append(pq.get())   # ✅ no candidates needed

        print("Current Beam:")
        for cost, path in beam:
            print(f"  path={path}  cost={cost}")
        print()

    print("Goal not found")
beam_search(start='S', goal='L', beam_width=3)