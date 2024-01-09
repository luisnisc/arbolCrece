# ArbolCrece

ArbolCrece es un módulo de Python que implementa un árbol binario de búsqueda (BST). Proporciona funciones para insertar, eliminar y añadir nodos en el árbol de manera ordenada.

## Clases

### TreeNode

La clase `TreeNode` representa un nodo en el árbol. Cada nodo tiene una clave (`key`) y dos hijos (`left` y `right`).

## Funciones

### insert(root, key)

La función `insert` inserta un nuevo nodo con la clave dada en el árbol. Si la clave es menor que la clave del nodo raíz, se inserta en el subárbol izquierdo. Si la clave es mayor, se inserta en el subárbol derecho.

### delete(root, key)

La función `delete` elimina el nodo con la clave dada del árbol. Si la clave es menor que la clave del nodo raíz, busca en el subárbol izquierdo. Si la clave es mayor, busca en el subárbol derecho.

### add_ordered_nodes(root, num_nodes)

La función `add_ordered_nodes` inserta un número dado de nuevos nodos en el árbol. Los nodos se insertan en orden, y cada nuevo nodo se convierte en la raíz de un subárbol donde se insertan los siguientes dos nodos. Los nodos añadidos son números aleatorios entre 10 y 100.
