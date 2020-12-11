#!/usr/bin/env python3
from itertools import count


EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def count_occupied(area, x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

    cnt = 0
    for dir_x, dir_y in directions:
        new_x = x + dir_x
        new_y = y + dir_y

        if (
            0 <= new_y < len(area)
            and 0 <= new_x < len(area[0])
            and area[new_y][new_x] == OCCUPIED
        ):
            cnt += 1
    return cnt


def tick(area):
    new_area = []
    for y, row in enumerate(area):
        new_row = ''
        for x, c in enumerate(row):
            num_children = count_occupied(area, x, y)
            if c == EMPTY and num_children == 0:
                new_row += OCCUPIED
            elif c == OCCUPIED and num_children >= 4:
                new_row += EMPTY
            else:
                new_row += c
        new_area.append(new_row)
    return new_area


def compute(cts: str):
    area = cts.splitlines()

    for i in count(1):
        new_area = tick(area)
        if new_area == area:
            return sum(1 for row in area for c in row if c == OCCUPIED)
        area = new_area


def main() -> int:
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
