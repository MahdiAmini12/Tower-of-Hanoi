import cv2 as cv
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np



cap = cv.VideoCapture(0)#? 0 means first webcame
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.mp4', fourcc, 24.0, (640, 480))

while(True):
    ret, frame = cap.read()
    color = cv.cvtColor(frame, cv.COLOR_RGB2BGR)#? cvtColor = convert color
    out.write(frame)

    cv.imshow('webcam', color)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release
cv.destroyAllWindows()


cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volMin,volMax = volume.GetVolumeRange()[:2]

while True:
    ssuccess,img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB) #finds location of xyz of hands

    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark):
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)

    if lmList != []:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]

        cv.circle(img,(x1,y1),4,(255,0,0),cv.FILLED)
        cv.circle(img,(x2,y2),4,(255,0,0),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,0),3)

        length = hypot(x2-x1,y2-y1)

        vol = np.interp(length,[15,220],[volMin,volMax])
        print(vol,length)
        volume.SetMasterVolumeLevel(vol, None)

            #hand range 15 - 220
            #Volume range -63.5 - 0.0

    cv.imshow('Image',img)
    if cv.waitKey(1) & 0xff == ord('q'):
        break



cap = cv2.VideoCapture(0)#? 0 means first webcame
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 24.0, (640, 480))

while(True):
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)#? cvtColor = convert color
    out.write(frame)

    cv2.imshow('webcam', color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release
cv2.destroyAllWindows()