
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root
def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root
root = None
keys = [5, 3, 7, 2, 4, 6, 8], [5], [6]
for key in keys:
    root = insert(root, key)
import graphviz
def visualize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')

import random

def add_ordered_nodes(root, num_nodes):
    # Inserta nuevos nodos en orden
    for i in range(num_nodes):
        # Genera un número aleatorio entre 10 y 100 para el nuevo nodo
        new_key = random.randint(10, 100)
        # Inserta el nuevo nodo
        root = insert(root, new_key)  # Pasa la raíz al llamar a insert
        # Si hay más nodos por insertar, los inserta en el subárbol de este nodo
        if i + 1 < num_nodes:
            root.left = insert(root.left, random.randint(10, 100))
            if i + 2 < num_nodes:
                root.right = insert(root.right, random.randint(10, 100))
            # Avanza el contador para reflejar los nodos que acabamos de insertar
            i += 2
    return root

root = None
keys = [5, 3, 7, 2, 4, 6, 8]
for key in keys:
    root = insert(root, key)
visualize_binary_tree(root)
root = add_ordered_nodes(root, 5)
visualize_binary_tree(root)