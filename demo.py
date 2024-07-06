# import cv2
# import mediapipe as mp
# import math
# # import numpy as np

# radiusDrawPoint = 12
# radiusCheckCollide = 18 
# radiusDeletePoint = 45
# indexDrawPoint = 8
# checkPoint1Idx = 12
# maxRadiusCheckPoint = 35
# fileDraw = 'demo.jpg'
# imgDraw = cv2.imread(fileDraw)
# colorDraw = (0, 225, 0)
# fileResult = 'image.jpg'
# points = []

# def readImgCam(cap):
#     (ret, img) = cap.read()
#     img = cv2.flip(img, 1)
#     return img

# def findHands(img, hand):
#     global radiusCheckCollide
#     global imgDraw
#     results = hand.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     h, w, c = img.shape

#     if results.multi_hand_landmarks:
#         for lm in results.multi_hand_landmarks[0].landmark:
#             cx, cy = int(lm.x*w), int(lm.y*h)
#             cv2.circle(img, (cx, cy), radiusCheckCollide, (225, 225, 225), 1)
#             mp.solutions.drawing_utils.draw_landmarks(img, results.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)

#         imgDraw = pointManagement(img, results)

#     return img

# def createDrawPoint(img, cx, cy):
#     global radiusDrawPoint
#     global colorDraw
    
#     cv2.circle(img, (cx, cy), radiusDrawPoint, colorDraw, cv2.FILLED)
#     return img

# def createPointMove(img, cx, cy):
#     global radiusDrawPoint
    
#     cv2.circle(img, (cx, cy), radiusDrawPoint + 12, (0, 225, 225), cv2.FILLED)
#     return img

# def createDeletePoint(img, cx, cy):
#     global radiusDeletePoint

#     cv2.circle(img, (cx, cy), radiusDeletePoint, (0, 0 , 0), cv2.FILLED)
#     return img

# def pointManagement(img, results):
#     global radiusDrawPoint
#     global checkPoint1Idx
#     global indexDrawPoint
#     global fileDraw
#     global imgDraw
#     global points

#     h, w, c = img.shape
#     lm0 = results.multi_hand_landmarks[0].landmark[8] #8
#     lm1 = results.multi_hand_landmarks[0].landmark[12] #8
#     lm2 = results.multi_hand_landmarks[0].landmark[16] #8
#     cx0, cy0 = int(lm0.x * w), int(lm0.y * h)
#     cx1, cy1 = int(lm1.x * w), int(lm1.y * h)
#     cx2, cy2 = int(lm2.x * w), int(lm2.y * h)
#     dist1 = math.sqrt((cx0 - cx1) ** 2 + (cy0 - cy1) ** 2)
#     dist2 = math.sqrt((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2)
    
#     if dist1 <= maxRadiusCheckPoint and dist2 > maxRadiusCheckPoint:
#         createPointMove(img, cx1, cy1)
#         points.clear()
#     elif dist1 <= maxRadiusCheckPoint and dist2 <= maxRadiusCheckPoint:
#         createDeletePoint(img, cx1, cy1)
#         imgDraw = delete(imgDraw, cx1, cy1)
#     else:
#         createDrawPoint(img, cx0, cy0)
#         # if len(lmList) > 1:
#         #     points.append(lmList[8][1:])
#         imgDraw = draw(imgDraw, cx0, cy0)
        
#             # print(startPoint, endPoint)
#     return imgDraw

# def draw(imgDraw, cx, cy):
#     global colorDraw
#     global radiusDrawPoint
#     global points

#     points.append([cx, cy])
#     for ptIdx in range(len(points) - 1):
#             startPoint = points[ptIdx]
#             endPoint = points[ptIdx + 1]
#             if startPoint != endPoint:
#                 cv2.line(imgDraw, startPoint, endPoint, colorDraw, thickness = radiusDrawPoint)
#     # cv2.circle(imgDraw, (cx, cy), radiusDrawPoint, colorDraw, cv2.FILLED)

#     return imgDraw

# def delete(imgDraw, cx, cy):
#     global radiusDeletePoint
#     global points
   
#     points.clear()
#     points.append([cx, cy])
#     for ptIdx in range(len(points) - 1):
#         startPoint = points[ptIdx]
#         endPoint = points[ptIdx + 1]
#         if startPoint != endPoint:
#             cv2.line(imgDraw, startPoint, endPoint, colorDraw, thickness = radiusDrawPoint)
#     cv2.circle(imgDraw, (cx, cy), radiusDeletePoint, (0, 0, 0), cv2.FILLED)

#     return imgDraw

# def main():
#     global imgDraw
#     global fileDraw

#     cap = cv2.VideoCapture(0)
#     img = cv2.imread('image.jpg')
#     hands = mp.solutions.hands.Hands()

#     while cap.isOpened():
#         img = readImgCam(cap)
#         img = findHands(img, hands)
#         img = cv2.add(img, imgDraw)        
#         cv2.imshow('Image', img)
#         cv2.imshow('img draw',imgDraw)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cv2.imwrite(fileDraw, imgDraw)
#     cap.release()
#     cv2.destroyAllWindows()

# img = cv2.imread('demo.jpg')
# h, w, c = img.shape
# cv2.rectangle(img, (0, 0), (w, h), (0, 0, 0), cv2.FILLED)
# cv2.imwrite('demo.jpg', img)

# main()