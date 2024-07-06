import cv2

class Point:
    def __init__(self, color, radius:int):
        self.color = color
        self.radius = radius

    def showPoint(self, img, x, y):
        cv2.circle(img, (x, y), self.radius, self.color, cv2.FILLED)
        
        return img
