# Recursively traverse the dictionary [node] to find occurrences of [kv] key and output their values


def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
                yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x


d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'nested_key1': {'inner_key_1': 'inner_val_1',
                                                                           'inner_key_2': 'inner_val_2', 'innerkey': 'innerval-d'}, 'nested_key2': [{'l_key_1': 'l_val_1'}, {'innerkey': 'innerval-d-l'}]}


for node in d.values():
    print(list(findkeys(node, 'innerkey')))
