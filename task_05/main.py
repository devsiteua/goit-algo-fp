import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def build_heap_tree(heap_values, index=0):
    if index >= len(heap_values):
        return None

    node = Node(heap_values[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap_values, left_index)
    node.right = build_heap_tree(heap_values, right_index)

    return node


def get_color(index, total):
    if total == 1:
        intensity = 220
    else:
        intensity = 50 + int(180 * index / (total - 1))

    return f"#{intensity:02x}{intensity:02x}ff"


def set_traversal_colors(order):
    total = len(order)

    for index, node in enumerate(order):
        node.color = get_color(index, total)


def reset_colors(tree_root):
    if tree_root is None:
        return

    stack = [tree_root]

    while stack:
        node = stack.pop()
        node.color = "skyblue"

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


def dfs_traversal(tree_root):
    if tree_root is None:
        return []

    order = []
    stack = [tree_root]

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return order


def bfs_traversal(tree_root):
    if tree_root is None:
        return []

    order = []
    queue = deque([tree_root])

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return order


def print_order(title, order):
    values = [str(node.val) for node in order]
    print(f"{title}: {' -> '.join(values)}")


def run_tests():
    tree_root = build_heap_tree([1, 2, 3, 4, 5, 6, 7])

    dfs_order = dfs_traversal(tree_root)
    bfs_order = bfs_traversal(tree_root)

    assert [node.val for node in dfs_order] == [1, 2, 4, 5, 3, 6, 7]
    assert [node.val for node in bfs_order] == [1, 2, 3, 4, 5, 6, 7]

    set_traversal_colors(dfs_order)
    colors = [node.color for node in dfs_order]
    assert len(colors) == len(set(colors))
    assert colors[0].startswith("#")


def main():
    run_tests()

    values = [1, 4, 7, 20, 10, 15, 9, 30, 25]
    tree_root = build_heap_tree(values)

    dfs_order = dfs_traversal(tree_root)
    set_traversal_colors(dfs_order)
    print_order("DFS order", dfs_order)
    draw_tree(tree_root)

    reset_colors(tree_root)

    bfs_order = bfs_traversal(tree_root)
    set_traversal_colors(bfs_order)
    print_order("BFS order", bfs_order)
    draw_tree(tree_root)


if __name__ == "__main__":
    main()
