import cv2

def process_something(frame):

    return frame

def read_video(path):
    video=cv2.VideoCapture(path)
    while True:
        state, frame=video.read()
        if not state:
            continue
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(1)== ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    read_video(r"C:\Users\Pc\Downloads\WhatsApp Video 2024-09-18 at 19.16.42.mp4")