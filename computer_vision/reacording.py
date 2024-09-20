import cv2
from datetime import datetime

def add_datetime(frame):
    cdate=datetime.now().strftime("%d-%x-%y %H:%M:%S")
    h,w,_=frame.shape
    frame=cv2.putText(
        frame,cdate,(20,h-20),
        cv2.FONT_HERSHEY_SIMPLEX,
        .75,(0,155,255),
    )
    return frame

def read_webcam(idx=0):
    video=cv2.VideoCapture(idx)
    codec=cv2.VideoWriter_fourcc(*"XVID")
    writer=cv2.VideoWriter("output.avi",codec,25,(640,480))
    while True:
        state, frame=video.read()
        if not state:
            break

        frame=add_datetime(frame)
        cv2.imshow("frame",frame)
        writer.write(frame)
        if cv2.waitKey(1)== ord("q"):
            break
    video.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    read_webcam()