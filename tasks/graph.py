from collections import deque
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]: #depth
        to_visit = [self._root]
        visited = []
        while to_visit:
            node = to_visit.pop(-1)
            if node in visited:
                continue
            if node.outbound:
                to_visit.extend(reversed(node.outbound))
            visited.append(node)
        return list(visited)


    def bfs(self) -> list[Node]: #breadth
        to_visit = [self._root]
        visited = []
        while to_visit:
            node = to_visit.pop(0)
            if node in visited:
                continue
            if node.outbound:
                to_visit.extend(node.outbound)
            visited.append(node)
        return visited


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(d)
a.point_to(c)
g = Graph(a)

print(g.bfs())
#assert g.bfs() == ['a', 'b', 'c', 'd']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(d)
a.point_to(c)
g = Graph(a)

print(g.dfs())
#assert g.dfs() == [a, b, d, c]
