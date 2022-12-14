
from itertools import chain, combinations


def powerset(iterable):
    l = list(iterable)
    return chain.from_iterable(combinations(l, r) for r in range(len(l) + 1))

def time_to_str(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return '{0}:{1}:{2}'.format(int(hours),int(mins),sec)