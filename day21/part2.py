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

    map_inverse = defaultdict(set)
    for allergen, ingredients in map_candidates.items():
        for ingredient in ingredients:
            map_inverse[ingredient].add(allergen)

    resolved_ingredients = {}

    while map_inverse:
        for ingredient, allergens in list(map_inverse.items()):
            if len(allergens) == 1:
                map_inverse.pop(ingredient)

                allergen = allergens.pop()
                resolved_ingredients[ingredient] = allergen

                for other_allergens in map_inverse.values():
                    if allergen in other_allergens:
                        other_allergens.remove(allergen)

    return ','.join(
        x for x, _ in sorted(resolved_ingredients.items(), key=lambda x: x[1])
    )


TEST_1 = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


def test_compute():
    assert compute(TEST_1) == 'mxmxvkd,sqjhc,fvjkl'


def main():
    with open('input.txt', 'r') as f:
        cts = f.read().strip()

    print(compute(cts))

    return 0


if __name__ == '__main__':
    exit(main())
