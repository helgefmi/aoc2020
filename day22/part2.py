#!/usr/bin/env python3


def parse_decks(cts):
    players = cts.split('\n\n')

    ret = []
    for player in players:
        ret.append([int(n) for n in player.splitlines()[1:]])
    return ret


def play_game(decks):
    mem = set()

    while all(decks):
        key = str(decks)
        if key in mem:
            return 0
        mem.add(key)

        a, b = decks[0].pop(0), decks[1].pop(0)

        if a <= len(decks[0]) and b <= len(decks[1]):
            winner = play_game([decks[0][:a], decks[1][:b]])
        else:
            winner = 0 if a > b else 1

        decks[winner].extend([a, b] if winner == 0 else [b, a])
    return 0 if decks[0] else 1


def compute(cts):
    decks = parse_decks(cts)

    winner = play_game(decks)
    winning_deck = decks[winner]

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
    assert compute(TEST_1) == 291


def main():
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
