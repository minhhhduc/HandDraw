from point.PointDraw import *
from point.Point import *
import math


class PointManagement:
    def __init__(self, imgDraw, colorDraw, colorMove, colorDelete, 
                 radiusDrawPoint, radiusMove, radiusDeletePoint,
                 pointsDraw, PointsDelete, maxRadiusCheckPoint) -> None:
        self.imgDraw = imgDraw
        self.maxRadiusCheckPoint = maxRadiusCheckPoint
        self.pointDraw = self.createPointDraw(colorDraw, radiusDrawPoint, pointsDraw)
        self.pointMove = self.createPointMove(colorMove, radiusMove)
        self.pointDelete = self.createPointDelete(colorDelete, radiusDeletePoint, PointsDelete)

    def createPointDraw(self, color, radius, points):
        return PointDraw(color, radius, points)
    
    def createPointDelete(self, color, radius, points):
        return PointDraw(color, radius, points)
    
    def createPointMove(self, color, radius):
        return Point(color, radius)
    
    def pointManagement(self, img, results):
        h, w, c = img.shape
        lm0 = results.multi_hand_landmarks[0].landmark[8] #8
        lm1 = results.multi_hand_landmarks[0].landmark[12] #8
        lm2 = results.multi_hand_landmarks[0].landmark[16] #8
        cx0, cy0 = int(lm0.x * w), int(lm0.y * h)
        cx1, cy1 = int(lm1.x * w), int(lm1.y * h)
        cx2, cy2 = int(lm2.x * w), int(lm2.y * h)
        dist1 = math.sqrt((cx0 - cx1) ** 2 + (cy0 - cy1) ** 2)
        dist2 = math.sqrt((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2)
    
        if dist1 <= self.maxRadiusCheckPoint and dist2 > self.maxRadiusCheckPoint:
            self.pointMove.showPoint(img, cx1, cy1)
            self.pointDelete.reset()
            self.pointDraw.reset()
            
        elif dist1 <= self.maxRadiusCheckPoint and dist2 <= self.maxRadiusCheckPoint:
            self.pointDelete.showPoint(img, cx1, cy1)
            self.pointDraw.reset()
            self.imgDraw = self.pointDelete.draw(self.imgDraw, cx1, cy1)
        else:
            self.pointDelete.reset()
            self.pointDraw.showPoint(img, cx0, cy0)
            # if len(lmList) > 1:
            #     points.append(lmList[8][1:])
            self.imgDraw = self.pointDraw.draw(self.imgDraw, cx0, cy0)
            
                # print(startPoint, endPoint)
        return self.imgDraw
    
