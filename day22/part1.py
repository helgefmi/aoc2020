#!/usr/bin/env python3


def parse_decks(cts):
    players = cts.split('\n\n')

    ret = []
    for player in players:
        ret.append([int(n) for n in player.splitlines()[1:]])
    return ret


def play_game(decks):
    while all(decks):
        a, b = decks[0].pop(0), decks[1].pop(0)
        winner = decks[0] if a > b else decks[1]
        winner.extend([a, b] if a > b else [b, a])
    return decks[0] or decks[1]


def compute(cts):
    decks = parse_decks(cts)

    winning_deck = play_game(decks)

    winning_deck.reverse()
    return sum(a * b for a, b in enumerate(winning_deck, start=1))


TEST_1 = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


def test_compute():
    assert compute(TEST_1) == 306


def main():
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
