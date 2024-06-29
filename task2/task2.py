from math import isclose, sqrt
from math import pow as mpow
from typing import List, Optional, Tuple
import sys

class Point():
    def __init__(self, x: float|int, y: float|int):
        self.x = x
        self.y = y
    

class Circle():
    def __init__(self, center: Point, radius: float|int):
        self.center = center
        self.radius = radius

class Solution():
    def __init__(self, fp_to_circle: str, fp_to_points: str):
        self.filepath_to_circle = fp_to_circle
        self.filepath_to_points = fp_to_points

        self.circle = self.__read_circle_file()
        self.points = self.__read_points_file()
    
    def __read_circle_file(self) -> Tuple[Tuple|float]:
        with open(self.filepath_to_circle, 'r') as f:
            coords = tuple(map(float, f.readline().strip().split()))
            radius = float(f.readline().strip())
        return Circle(Point(*coords), radius=radius)

    def __read_points_file(self) -> List[Tuple[float]]:
        with open(self.filepath_to_points, 'r') as f:
            lines = [line.strip().split() for line in f.readlines()]
        return [Point(float(x), float(y)) for x, y in lines]

    def get_points_cirle_intersections(self, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> int:
        '''
        Returns if point intersects, includes or excludes cirlce.
        :param rel_tol: Same as math.isclose parameter.
        :param abs_tol: Same as math.isclose parameter.
        :return: Returns one of 3 cases: 0 - point on circle, 1 - point inside the circle, 2 - point outside the circle.
        '''
        intersection_statuses: List[int] = []
        for point in self.points:
            distance_vector = (point.x - self.circle.center.x, point.y - self.circle.center.y)
            distance = sqrt(mpow(distance_vector[0], 2) + mpow(distance_vector[1], 2))

            if isclose(distance, self.circle.radius, rel_tol=rel_tol, abs_tol=abs_tol):
                intersection_statuses.append(0)
                continue
        
            intersection_statuses.append((distance > self.circle.radius) + 1)
        
        return intersection_statuses

if __name__ == "__main__":
    solution = Solution(*sys.argv[1:3])
    output = solution.get_points_cirle_intersections()
    print(*output, sep='\n')