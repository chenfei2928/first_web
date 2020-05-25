import cv2

# 摄像头代码

video = cv2.VideoCapture(0)
while 1:
    ret,frame = video.read()
    new_frame = cv2.resize(frame,(450,280))
    cv2.imshow("video",new_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()