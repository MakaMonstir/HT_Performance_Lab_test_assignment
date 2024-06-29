import math
import sys

class Solution():
    def __init__(self, fp_to_nums: str):
        self.filepath = fp_to_nums
        self.nums = self.__read_nums()
    
    def __read_nums(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
        
        return [int(line.strip()) for line in lines]
    
    def print_minimal_steps_count(self):
        average = sum(self.nums) / len(self.nums)
        closest_num = min(self.nums, key=lambda x: abs(x - average))
        steps = sum(map(lambda x: abs(x - closest_num), self.nums))

        print(steps)

if __name__ == '__main__':
    solution = Solution(sys.argv[1])
    solution.print_minimal_steps_count()
    