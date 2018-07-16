# -*- coding: utf-8 -*-

import cv2
def getFaceImage():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("image/faceID.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()


def getFruitImage():
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cv2.imwrite("image/fruit.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":


    cv2.namedWindow("capture", 0)
    cv2.resizeWindow('capture', 1280,960)
    cv2.moveWindow('capture',0,0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        #

        cv2.imshow("capture",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
'''     
    getFruitImage()

    print 'camera main task'
'''