import cv2
import mediapipe as mp
from point.PointManager import *

class Decorator:
    def __init__(self, radiusCheckCollide, imgDraw,
                 colorDraw, colorMove, colorDelete, 
                 radiusDrawPoint, radiusMove, radiusDeletePoint,
                 pointsDraw : list, PointsDelete : list, maxRadiusCheckPoint):
        self.color = (225, 225, 225)
        self.radiusCheckCollide = radiusCheckCollide
        self.imgDraw = imgDraw
        self.pointManagement = PointManagement(self.imgDraw,
                 colorDraw, colorMove, colorDelete, 
                 radiusDrawPoint, radiusMove, radiusDeletePoint,
                 pointsDraw, PointsDelete, maxRadiusCheckPoint) 

    def findHand(self, img, hand):
        results = hand.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        h, w, c = img.shape

        if results.multi_hand_landmarks:
            for lm in results.multi_hand_landmarks[0].landmark:
                cx, cy = int(lm.x*w), int(lm.y*h)
                cv2.circle(img, (cx, cy), self.radiusCheckCollide, (225, 225, 225), 1)
                mp.solutions.drawing_utils.draw_landmarks(img, results.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)

            # imgDraw = self.pointManagement(img, results)
            self.imgDraw = self.pointManagement.pointManagement(img, results)
        return img
    
class Main:
    def __init__(self) -> None:
        self.radiusDrawPoint = 5
        self.radiusCheckCollide = 20 
        self.radiusDeletePoint = 45
        self.indexDrawPoint = 8
        self.checkPoint1Idx = 2 * self.radiusCheckCollide
        self.maxRadiusCheckPoint = 2 * self.radiusCheckCollide
        self.fileDraw = 'FileDraw.jpg'
        self.imgDraw = cv2.imread(self.fileDraw)
        self.colorDraw = (0, 225, 0)
        self.colorMove = (0, 225, 225)
        self.colorDelete = (0, 0, 0)
        self.radiusMove = self.radiusDrawPoint + 12
        self.decorator = Decorator(self.radiusCheckCollide, self.imgDraw,
                                   self.colorDraw, self.colorMove, self.colorDelete,
                                   self.radiusDrawPoint, self.radiusMove, 
                                   self.radiusDeletePoint, [], [], self.maxRadiusCheckPoint)

    def readImgCam(self, cap):
        (ret, img) = cap.read()
        img = cv2.flip(img, 1)
        return img
    
    def initImgDraw(self):
        img = cv2.imread(self.fileDraw)
        h, w, c = img.shape
        cv2.rectangle(self.imgDraw, (0, 0), (w, h), self.colorDelete, cv2.FILLED)

    def __main__(self):
        cap = cv2.VideoCapture(0)
        hands = mp.solutions.hands.Hands()
        self.initImgDraw()

        while cap.isOpened():
            img = self.readImgCam(cap)
            img = self.decorator.findHand(img, hands)
            img = cv2.add(img, self.imgDraw)
            cv2.imshow('Img', img)
            cv2.imshow('ImgDraw', self.imgDraw)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cv2.imwrite(self.fileDraw, self.imgDraw)
        cap.release()
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    main = Main()
    main.__main__()
