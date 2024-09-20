import cv2

def process_something(frame):

    return frame

def read_webcam(idx=0):
    video=cv2.VideoCapture(idx)
    while True:
        state, frame=video.read()
        if not state:
            break
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(1)== ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    read_webcam()