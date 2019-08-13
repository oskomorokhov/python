#!/usr/bin/env checkio --domain=py run node-disconnected-users2

# https://py.checkio.org/mission/node-disconnected-users2/

#
# END_DESC


def disconnected_users(net, users, source, crushes):

    nodes = list(users.keys())


<< << << < HEAD
    paths, graph = ([], {})

    for item in net:
        graph[item[0]] = graph.get(item[0], '')+item[1]
== == == =
    paths = []
    graph = {}

    for item in net:
        if item[0] in graph: graph[item[0]] += item[1]
        else: graph[item[0]] = [item[1]]
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e

    for node in crushes:
        if node in graph: del graph[node]

    for node in nodes:
        paths.append(find_path(graph, source, node))

    count = 0

    for node in crushes:
        for num, path in enumerate(paths):
<< << << < HEAD
            if not path: count += users.get(nodes[paths.index(None, num)])
== == == =
            if path == None: count += users.get(nodes[paths.index(None, num)])
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
            elif node in path: count += users.get(node)

    return count
    
<<<<<<< HEAD
def find_path(graph, start, end, path=None, count=None):
        if path is None: path=[] 
        if count is None: count=[0,0]
        
        path=path+[start]
		
		if start == end:
			return path
            
		if not start in graph:
			count[1]+=1
			return
            
		for node in graph[start]:
			if node not in path:
				count[0]+=1
=======
def find_path(graph, start, end, path=[], count=None):
    	
        if count is None: count=[0,0]
		path = path + [start]
		
		if start == end:
			return path
		if not start in graph:
			count[1]+=1
			
			return None
		for node in graph[start]:
			if node not in path:
				count[0]+=1
				#
>>>>>>> 98fa6ff036ccfeb62253c60979fda532adc48e6e
				newpath = find_path(graph, node, end, path, count)
				if newpath: return newpath
			else:
				count[1]+=1
<<<<<<< HEAD
=======
		return None	
>>>>>>> 98fa6ff036ccfeb62253c60979fda532adc48e6e

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    
<<<<<<< HEAD
    assert disconnected_users([["A","B"],["A","C"],["A","D"],["A","E"],["A","F"]],{"A":10,"C":10,"B":10,"E":10,"D":10,"F":10},"A",["B","C"]) == 20

    
=======
>>>>>>> 98fa6ff036ccfeb62253c60979fda532adc48e6e
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"
    
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"
    
    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"
       
    assert disconnected_users([["A","B"],["B","C"],["C","D"]],{"A":10,"C":30,"B":20,"D":40},"A",["D"]) == 40

    print('Done. Try to check now. There are a lot of other tests')
