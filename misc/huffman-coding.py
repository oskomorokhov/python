# huffman coding / min heap

#from binarytree import Node


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value
        self.left = left    # Left child
        self.right = right  # Right child


def Tinsert(node, value):
    if node is None:
        print("INSERT: inserting item", value, "as NEW NODE")
        node = Node(value)
    else:
        if value < node.value:
            print("INSERT:", value, "<", node.value, "recur LEFT")
            node.left = Tinsert(node.left, value)
            # print "LEFT child of",node[0].value,"is now",value
        if value > node.value:
            print("INSERT:", value, ">", node.value, "recur RIGHT")
            node.right = Tinsert(node.right, value)
            # print "RIGHT child of",node[0].value,"is now",value
    # print(node)
    return node


text = "The ugliest code in the entire galaxy!"
text_arr = list(text)


frequency_arr = []
for i in text_arr:
    frequency_arr.append((text_arr.count(i), i))

frequency_arr.sort()
q = list(set(frequency_arr[:]))
q.sort()
print('sorted frequency array', q)

z = []
d = {}
c = 0
while len(q) > 1:
    m1 = min(q)
    q.remove(m1)
    m2 = min(q)
    print(m1, m2)
    node = (m1[0]+m2[0], m1[1]+m2[1])
    d[c] = Node(node)
    d[c].left = m1
    d[c].right = m2
    z.append(node)
    c += 1
else:
    # c+=1
    q.append(min(z))
    z.remove(min(z))
    m3 = min(q)
    q.remove(m3)
    m4 = min(q)
    node = (m3[0]+m4[0], m3[1]+m4[1])
    d[c] = Node(node)
    d[c].left = m3
    d[c].right = m4
    z.append(node)
