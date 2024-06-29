import sys
from typing import List, Optional
from itertools import cycle
from math import lcm

class Solution():
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m

    def get_circular_array_path(self) -> List[int]:
        circular_array = cycle(range(1, self.n + 1))
        result = []
        result_len = lcm(self.n, self.m - 1) // (self.m - 1)

        for _ in range(result_len - 1):
            result.append(next(circular_array))

            for _ in range(self.m - 2):
                next(circular_array)

        result.append(next(circular_array))

        return result

    def print_array(self) -> None:
        array = self.get_circular_array_path()
        print("".join(map(str, array)))

if __name__ == "__main__":
    solution = Solution(int(sys.argv[1]), int(sys.argv[2]))
    solution.print_array()