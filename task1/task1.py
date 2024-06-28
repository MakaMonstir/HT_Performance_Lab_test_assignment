from typing import List
from itertools import cycle
from math import lcm

def get_circular_array_path(n: int, m: int) -> List[int]:

    circular_array = cycle(range(1, n + 1))
    result = []
    result_len = lcm(n, m-1) // (m - 1)
    for _ in range(result_len - 1):
        result.append(next(circular_array))
        for _ in range(m - 2):
            next(circular_array)
    result.append(next(circular_array))

    return result

assert get_circular_array_path(4, 3) == [1, 3]
assert get_circular_array_path(5, 4) == [1, 4, 2, 5, 3]
assert get_circular_array_path(1, 2) == [1]