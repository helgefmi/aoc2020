#!/usr/bin/env python3
from collections import defaultdict


def parse_food_list(cts):
    ret = []
    for line in cts.splitlines():
        a, b = line.split(' (contains ')
        ingredients = set(a.split(' '))
        allergens = set(b[:-1].split(', '))
        ret.append((ingredients, allergens))
    return ret


def compute(cts):
    food_list = parse_food_list(cts)

    all_ingredients = set()
    all_allergens = set()
    for ingredients, allergens in food_list:
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)

    map_candidates = defaultdict(set)
    for allergen in all_allergens:
        map_candidates[allergen] = set(all_ingredients)

    for ingredients, allergens in food_list:
        for allergen in allergens:
            map_candidates[allergen] = map_candidates[allergen] & ingredients

    candidate_ingredients = set(
        ingredient
        for ingredients in map_candidates.values()
        for ingredient in ingredients
    )

    noncandidate_ingredients = all_ingredients - candidate_ingredients

    total = 0
    for ingredients, _ in food_list:
        total += len(noncandidate_ingredients & ingredients)
    return total


TEST_1 = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


def test_compute():
    assert compute(TEST_1) == 5


def main():
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
