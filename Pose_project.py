import cv2
import time
import PoseModule as pm

cap=cv2.VideoCapture("PoseVideos/video1.mp4")
pTime=0
detector=pm.poseDetector()
while(cap.isOpened()):
    while True:
        success,img=cap.read()
        img=detector.findPose(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[0])
            cv2.circle(img,(lmList[14][1],lmList[14][2]),15,(0,0,255),cv2.FILLED)
        img = cv2.resize(img, (1600, 900)) 
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,4,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choiceq
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
    #After the loop release the cap object
    cap.release()
    # Destroy all the windowsqqq
    cv2.destroyAllWindows()
else:
    print("Alert ! Camera disconnected")