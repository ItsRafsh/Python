



import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('rtsp://admin:1234@192.168.1.3:1935/')
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)        # ini membalik kan mirror nya yeayyy
    frame_height,frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width+2)       # hapus 2 untuk kembali default
                y = int(landmark.y*frame_height+2)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x = screen_width/frame_width*x             # 18
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside',abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow("Virtual Mouse",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

















# 
# import cv2
# from cvzone.HandTrackingModule import HandDetector

# cap = cv2.VideoCapture(0)
# detector = HandDetector(detectionCon=0.8,maxHands=2)


# while True:
#     sukses,img = cap.read()
#     hands, img =  detector.findHands(img)
#     # hands =  detector.findHands(img,draw=False)  # No draw

#     if hands:
#         hand1 = hands[0]
#         lmList1 = hand1["lmList"]
#         bbox1 = hand1["bbox"]
#         centerPoint1 = hand1["center"]
#         handType1 = hand1["type"]

#         jari1 =detector.fingersUp(hand1)
#         # lenght,info,img = detector.findDistance(lmList1[8],lmList1[12],img)
#         lenght, info = detector.findDistance(lmList1[8], lmList1[12])



#         if len(hands)==2:
#             hand2 = hands[1]
#             lmList2 = hand2["lmList"]
#             bbox2 = hand2["bbox"]
#             centerPoint2 = hand2["center"]
#             handType2 = hand2["type"]

#             jari2 =detector.fingersUp(hand2)
#             # print(jari1,jari2)

#     cv2.imshow("Image",img)
#     cv2.waitKey(1)
