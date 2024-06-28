import sys
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

def print_array(n: int, m: int) -> None:
    array = get_circular_array_path(n, m)
    print("".join(map(str, array)))

if __name__ == "__main__":
    arg_n, arg_m = sys.argv[1:]
    print_array(int(arg_n), int(arg_m))