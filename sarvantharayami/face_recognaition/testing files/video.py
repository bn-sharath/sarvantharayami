from importlib.resources import path
import os
import cv2

capture_obj = cv2.VideoCapture("http://192.168.0.104:8080/video")
count=0
while count<=20:
    r, frame = capture_obj.read()
    # print(capture_obj.read())
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("hello", frame)
    # s= cv2.imwrite(f"../saving/{count}.png",frame)
    # if s:
    #     print("saved")
    # else:
    #     print("not saved")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    pat="face_recognaition/saving/"
    try:
        cv2.imwrite(filename=pat+"hello"+str(count)+".jpeg",img=frame)
    except:
        print("not saving")
    count+=1

capture_obj.release()
cv2.destroyAllWindows()