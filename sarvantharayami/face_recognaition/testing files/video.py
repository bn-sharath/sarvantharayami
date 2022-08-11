import cv2

capture_obj = cv2.VideoCapture("http://192.168.0.101:8080/video")

while True:
    r, frame = capture_obj.read()
    cv2.imshow("hello", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture_obj.release()
cv2.destroyAllWindows()