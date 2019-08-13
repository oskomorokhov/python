# Find the largest number of "connected" colors in the grid
# A color is connected if it has same color to the left,right,bottom,or top of it
#
# input grid
colors = [['blue', 'yellow', 'white', 'green', 'green'],
          ['blue', 'blue', 'yellow', 'black', 'white'],
          ['red', 'red', 'black', 'black', 'black']]


def inspect_grid(arr):

    # same color neighbor count will go here
    count = {}

    # define coordinates for each node in grid
    for row_index, row in enumerate(arr):
        for node_index, node in enumerate(row):

            if not node in count.keys():
                count[node] = 1

            coords = (row_index, node_index)

            # go to subroutine to check all neighbor coords of current node
            result = check_neighbors(arr, node, coords)

            if result:
                # neighbor has same color, increment counter
                count[node] += result

    return max(count, key=count.get), max(count.values())


def check_neighbors(arr, node, coords, visited=set()):

    # we should check left, right, top and bottom neighbors:
    # left: row_index,node_index-1
    # right: row_index,node_index+1
    # top: row_index+1,node_index
    # bottom: row_index-1,node_index
    # 0<=row_index<=len(col)-1, 0<=node_index<=len(row)-1

    # unpack coords & define temp counter
    row_index, node_index = coords
    c = 0

    for ri, ni in ((row_index, node_index-1), (row_index, node_index+1), (row_index+1, node_index), (row_index-1, node_index)):

            # can't go beyond edges
        if (0 <= ri <= len(arr)-1 and 0 <= ni <= len(arr[0])-1):
                # compare with neighbor's value
            if node == arr[ri][ni]:
                if coords in visited:
                    # been there, seen (counted) it
                    return False
                else:
                    # we have a unique match
                    visited.add((coords))
                    c += 1
    else:
        return c


if __name__ == "__main__":
    print(inspect_grid(colors))
