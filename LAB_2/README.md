## 1 Задача
### обходы дерева

реализуем обход дерева in, pre, post - order с помощью рекурсии

#### pre-order
выводим сначала значение, затем идем по левым детям, потом по правым

```python
def dfs(i):
    if i == -1:
        return
    result.append(tree[i][0])
    dfs(tree[i][1])
    dfs(tree[i][2])
dfs(0)
```

пример 
```
        4
    2       5
  1   3    - - 
```
идем 4 2 1, возвращаемся к 2 и идем к 3ке, возвращаемся к корню и идем в правое поддерево, выводим 5

ответ `4 2 1 3 5`
#### post-order

сначала идем по левым детям, потом по правым и выводим значение

те выводим сначала значение всех своих детей и только потом свое значение
```python
result = []
def dfs(i):
    if i == -1:
        return
    dfs(tree[i][1])
    dfs(tree[i][2])
    result.append(tree[i][0])
dfs(0)
```
#### in-order
сначала идем по левым детям, потом выводим значение, потом по правым детям
```python
result = []
def dfs(i):
    if i == -1:
        return
    dfs(tree[i][1])
    result.append(tree[i][0])
    dfs(tree[i][2])

dfs(0)
```
---


## 3 Задача
### Добавление и поиск элемента БСТ

реализую простейшее БСТ на нодах 


```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

`self.left`, `self.right` хранят классы дочерних `Node`

`head = append_tree(head, val)` - Корень дерева, через который получаем доступ к остальным элементам БСТ

реализовал функцию добавления в дерево учитывая особенности дерева поиска
```python
def append_tree(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
         node.left = append_tree(node.left, value)
    else:
        node.right = append_tree(node.right, value)
    return node
```
- Если значение меньше значения узла, то идем влево, иначе направо.
- Если Ноды не существует, то создаем новую - Вставка успешна.
- рекурсивно поднимаемся к корню


Также реализовал поиск минимального элемента, больше `x`
```python
def find_min(node, x):
    if node is None:
        return float("inf")
    if x >= node.value:
        return find_min(node.right, x)
    if x < node.value:
        return min(node.value, find_min(node.left, x))
```
- Если значение узла меньше или равно `x` (не подходит), то идем вправо, т.к. там значения больше
- Если значение узла больше `x`, то идем влево и сравниваем с текущим значением, т.к. ищем минимально возможный элемент
- если узла нет, то возвращаем бесконечность


---
## 8 задача
### Максимальная высота дерева

на вход получаем двоичное дерево поиска, в виде `key`, `left`, `right`

чтобы найти высоту можно создать стэк, из которого будем брать и добавлять детей, прибавляя при этом высоту
```python
stack = [(1, 1)]
    while stack:
        node_index, height = stack.pop()
        max_height = max(max_height, height)

        left, right = nodes[node_index]
        if left != 0:
            stack.append((left, height + 1))
        if right != 0:
            stack.append((right, height + 1))
```

сравниваем с макс высотой
```python
max_height = max(max_height, height)
```
---

