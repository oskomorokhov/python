from queue import PriorityQueue


def dijkstra(graph: dict = None, start: str = None, end: str = None, queue: PriorityQueue = PriorityQueue(), visited: dict = {}) -> dict:
    """
    Find best path based on lowest cost
    """
    print("---foo start---")
    print("start", start)

    if graph is None or graph == {}:
        print("empty graph")
        return

    if not isinstance(start, tuple):
        # cost,node,via
        start = (0, start, None)

    if start[1] == end:
        # should shop processing arcs of this node
        print("target reached")
        visited[start[1]] = {'cost': start[0], 'via': start[2]}
        return visited

    if start[1] not in graph.keys():
        # mark as visited and backtrack
        print("dead end")
        visited[start[1]] = {'cost': start[0], 'via': start[2]}
        return

    if start not in queue.queue:
        _cost, _node, _via = start
        queue.put((_cost, _node, _via))

    print("we can go to", graph[start[1]].items())
    for node, value in graph[start[1]].items():
        print("node", node, "cost", value)
        #print("nodes in q",[n[1] for n in queue.queue])
        if node in visited.keys():
            print("node in visited, skip")
            continue
        entry = [e for e in queue.queue if node in e]
        if entry:
            print("node already in queue", entry[0])
            if start[0]+value < entry[0][0]:
                queue.queue.remove(entry[0])
                queue.put((start[0]+value, node, start[1]))
                print("updated priority for", (start[0]+value, node, start[1]))
                print("queue is", queue.queue)
        else:
            queue.put((start[0]+value, node, start[1]))
            print((start[0]+value, node, start[1]), "enqueued")
            print("queue is", queue.queue)

    _cost, _node, _via = queue.get()
    visited[_node] = {'cost': _cost, 'via': _via}

    print("done with & removed", (_cost, _node, _via), "from queue")
    print("queue is", queue.queue)
    print("visited", visited)

    for entry in queue.queue:
        print("q entry", entry)
        print("---recur start---")
        path = dijkstra(graph, entry, end, queue, visited)
        print("---recur end---")
        if path:
            return path

    print("---foo end---")
    return visited


graph = {'S': {'A': 7, 'B': 2, 'C': 3},
         'A': {'S': 7, 'B': 3, 'D': 4},
         'B': {'S': 2, 'A': 3, 'D': 4, 'H': 1},
         'C': {'S': 3, 'L': 2},
         'D': {'A': 4, 'B': 4, 'F': 5},
         'H': {'B': 1, 'F': 3, 'G': 2},
         'F': {'D': 5, 'H': 3},
         'G': {'H': 2, 'E': 3},
         'L': {'C': 2, 'I': 4, 'J': 4},
         'I': {'L': 4, 'J': 6, 'K': 4},
         'J': {'L': 4, 'I': 6, 'K': 4},
         'K': {'I': 4, 'J': 4, 'E': 5},
         'E': {'G': 2, 'K': 5, 'F': 2}
         }

if __name__ == "__main__":
    start = 'S'
    end = 'E'
    tree = dijkstra(graph, start, end)
    print(f"cost to reach {end} is {tree[end]['cost']}")
    print(tree)

    path = [end]

    key = end
    while tree[key]['via']:
        key = tree[key]['via']
        path.append(key)

    print(f"path is", path[::-1])
