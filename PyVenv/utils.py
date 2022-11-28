
from itertools import chain, combinations


def powerset(iterable):
    l = list(iterable)
    return chain.from_iterable(combinations(l, r) for r in range(len(l) + 1))