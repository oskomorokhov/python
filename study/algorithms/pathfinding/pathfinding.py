def find_path(graph, start, end, path=[], count=None):
    if count is None:
        count = [0, 0]
    print("-" * 40, "\nLooking for path between nodes", start, "->", end)
    path = path + [start]
    print(path)
    if start == end:
        print("-" * 40, "\nI have reached my destination!")
        print("It took me", sum(count), "steps total with",
              count[1], "backtracks, path length is", len(path))
        return path
    if not start in graph.keys():
        count[1] += 1
        print("Node has no arcs - dead end, backtracking")
        return None
    for node in graph[start]:
        if node not in path:
            count[0] += 1
            print("Going via arc", start, "->", node)
            newpath = find_path(graph, node, end, path, count)
            if newpath:
                return newpath
        else:
            count[1] += 1
            print(count[1])
            print("I have already visited", node, "node, backtracking")
            # if count[1]>len(graph): return "No valid path found."
    #print ("-" * 40),"\n","No valid path found."
    # print "END"
    return None


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'E', 'F', 'Z'],
         'D': ['C'],
         'F': ['C'],
         'W': ['I'],
         'Z': ['W']}


find_path(graph, 'A', 'U')
