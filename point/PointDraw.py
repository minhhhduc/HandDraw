import cv2
from point.Point import *

class PointDraw(Point):
    def __init__(self, color, radius, points : list):
        super().__init__(color, radius)
        self.points = points

    def draw(self, img, x, y):
        self.points.append([x, y])

        for ptIdx in range(len(self.points) - 1):
            startPoint = self.points[ptIdx]
            endPoint = self.points[ptIdx + 1]
            if startPoint != endPoint:
                cv2.line(img, startPoint, endPoint, self.color, thickness = self.radius * 2)
        
        return img
    
    def reset(self):
        self.points.clear()
        return self.points
