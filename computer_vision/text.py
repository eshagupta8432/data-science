import cv2

def process_something(frame):
    text="cutie"
    fs=1
    font=cv2.FONT_HERSHEY_SIMPLEX
    color=(255,255,255)
    thickness=2
    origin=(50,50)
    frame=cv2.putText(frame,text,origin,font,fs,color,thickness)
    return frame

def read_video(path):
    video=cv2.VideoCapture(path)
    while True:
        state, frame=video.read()
        if not state:
            break
        frame=process_something(frame)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1)== ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    read_video(r"C:\Users\Pc\Downloads\WhatsApp Video 2024-09-18 at 20.01.45.mp4")