from math import isclose, sqrt
from math import pow as mpow
from typing import List, Tuple
import sys

class Point():
    def __init__(self, x: float|int, y: float|int):
        self.x = x
        self.y = y
    

class Circle():
    def __init__(self, center: Point, radius: float|int):
        self.center = center
        self.radius = radius

def read_circle_file(file_path: str) -> Tuple[Tuple|float]:
    with open(file_path, 'r') as f:
        coords = tuple(map(float, f.readline().strip().split()))
        radius = float(f.readline().strip())
    return Circle(Point(*coords), radius=radius)

def read_points_file(file_path: str) -> List[Tuple[float]]:
    with open(file_path, 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]
    return [Point(float(x), float(y)) for x, y in lines]

def get_point_cirle_intersection(point: Point, circle: Circle, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> int:
    '''
    Returns if point intersects, includes or excludes cirlce.
    :param point: Point that would be checked.
    :param circle: Circle that would be checked.
    :param rel_tol: Same as math.isclose parameter.
    :param abs_tol: Same as math.isclose parameter.
    :return: Returns one of 3 cases: 0 - point on circle, 1 - point inside the circle, 2 - point outside the circle.
    '''
    distance_vector = (point.x - circle.center.x, point.y - circle.center.y)
    distance = sqrt(mpow(distance_vector[0], 2) + mpow(distance_vector[1], 2))

    if isclose(distance, circle.radius, rel_tol=rel_tol, abs_tol=abs_tol):
        return 0
    
    return (distance > circle.radius) + 1

if __name__ == "__main__":
    file_path_to_circle, file_path_to_points = sys.argv[1:]

    circle = read_circle_file(file_path_to_circle)
    points = read_points_file(file_path_to_points)

    for point in points:
        print(get_point_cirle_intersection(point=point, circle=circle))
    