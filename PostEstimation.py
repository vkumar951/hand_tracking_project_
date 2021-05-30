import cv2
import mediapipe as mp
import time 

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()
cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
cap=cv2.VideoCapture('PoseVideos/video1.mp4')
pTime=0
while(cap.isOpened()):
    while True:
        success,img=cap.read()
        img = cv2.resize(img, (960, 540)) 
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=pose.process(imgRGB)
        #print(results.pose_landmarks)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
            for id,lm in enumerate(results.pose_landmarks.landmark):
                h,w,c=img.shape
                print(id,lm)
                cx,cy=int(lm.x*w),int(lm.y*h)
                cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
                
        
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


