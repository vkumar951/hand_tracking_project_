import cv2
import mediapipe as mp
import time 
import handtracking_module as htm

pTime=0
cTime=0
cap=cv2.VideoCapture(0)
detector=htm.HandDetector()
while(cap.isOpened()):
    while True:
        success,img=cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img,draw=False)
        if len(lmList)!=0:
            print(lmList[4])
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choiceq
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
    #After the loop release the cap object   
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
else:
    print("Alert ! Camera disconnected")
