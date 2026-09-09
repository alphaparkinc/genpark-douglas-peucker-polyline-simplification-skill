"""
Autonomous Agent Douglas-Peucker Trajectory Simplification Skill
Pure Python Standard Library implementation.
"""
import math
from typing import List, Tuple, Dict, Any

class DouglasPeucker:
    """
    Douglas-Peucker polyline simplification algorithm.
    """
    @staticmethod
    def _point_line_dist(pt: Tuple[float, float], l1: Tuple[float, float], l2: Tuple[float, float]) -> float:
        dx = l2[0] - l1[0]
        dy = l2[1] - l1[1]
        line_len_sq = dx**2 + dy**2
        if line_len_sq < 1e-12:
            return math.hypot(pt[0] - l1[0], pt[1] - l1[1])
        cross = abs((pt[0] - l1[0]) * dy - (pt[1] - l1[1]) * dx)
        return cross / math.sqrt(line_len_sq)

    @staticmethod
    def simplify(points: List[Tuple[float, float]], epsilon: float) -> List[Tuple[float, float]]:
        if len(points) <= 2:
            return points

        max_dist = 0.0
        index = 0
        for i in range(1, len(points) - 1):
            d = DouglasPeucker._point_line_dist(points[i], points[0], points[-1])
            if d > max_dist:
                max_dist = d
                index = i

        if max_dist > epsilon:
            rec1 = DouglasPeucker.simplify(points[:index + 1], epsilon)
            rec2 = DouglasPeucker.simplify(points[index:], epsilon)
            return rec1[:-1] + rec2
        else:
            return [points[0], points[-1]]
