import cv2
import datetime
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

counter=0



while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    
    
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "Car_{}.png".format(counter)
        path = 'F:\car'
        cv2.imwrite(os.path.join(path , img_name), frame)
        print("{} written!".format(img_name))
        
        counter=counter+1
       

cam.release()

cv2.destroyAllWindows()
