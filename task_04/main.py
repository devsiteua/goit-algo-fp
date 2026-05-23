import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt


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
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
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


def is_min_heap(heap_values):
    for index in range(len(heap_values)):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap_values):
            if heap_values[index] > heap_values[left_index]:
                return False

        if right_index < len(heap_values):
            if heap_values[index] > heap_values[right_index]:
                return False

    return True


def visualize_heap(values):
    heap_values = values.copy()
    heapq.heapify(heap_values)

    print("Input values:")
    print(values)

    print("\nHeap array:")
    print(heap_values)

    heap_root = build_heap_tree(heap_values)
    draw_tree(heap_root)


def run_tests():
    values = [10, 4, 15, 20, 1, 7, 9]
    heapq.heapify(values)

    assert is_min_heap(values)

    heap_root = build_heap_tree(values)
    assert heap_root.val == values[0]
    assert heap_root.left.val == values[1]
    assert heap_root.right.val == values[2]


def main():
    run_tests()

    values = [10, 4, 15, 20, 1, 7, 9, 30, 25]
    visualize_heap(values)


if __name__ == "__main__":
    main()
