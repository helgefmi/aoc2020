#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.value)

    def iter(self):
        yield self

        node = self.next
        while node is not self:
            yield node
            node = node.next

    def find_value(self, value):
        for node in self.iter():
            if node.value == value:
                return node


def parse_nodes(cts):
    nodes = {}

    prev_n = None
    for n in cts:
        n = int(n)
        nodes[n] = Node(n)
        if prev_n:
            nodes[prev_n].next = nodes[n]
        prev_n = n

    for n in range(10, 1000000 + 1):
        nodes[n] = Node(n)
        nodes[prev_n].next = nodes[n]
        prev_n = n

    first_node = nodes[int(cts[0])]
    nodes[prev_n].next = first_node

    return first_node, nodes


def compute(cts):
    current, nodes = parse_nodes(cts)

    for _ in range(10000000):
        pick_up = [current.next, current.next.next, current.next.next.next]
        current.next = pick_up[-1].next

        pick_up_values = [x.value for x in pick_up]
        destination = current.value - 1
        while not destination or destination in pick_up_values:
            if destination == 0:
                destination = 1000000
            else:
                destination -= 1

        destination_node = nodes[destination]
        destination_node.next, pick_up[-1].next = pick_up[0], destination_node.next

        current = current.next

    one_cup = nodes[1]
    return one_cup.next.value * one_cup.next.next.value


def test_compute():
    assert compute('389125467') == 149245887792


def main():
    print(compute('137826495'))

    return 0


if __name__ == '__main__':
    exit(main())
