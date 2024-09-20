import cv2

def add_filters(frame):
    bw_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("bw_frame",bw_frame)
    cv2.imshow("rgb_frame",rgb_frame)

    return frame

def read_video(path):
    video=cv2.VideoCapture(path)
    while True:
        state, frame=video.read()
        if not state:
            continue
        
        
        frame=add_filters(frame)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1)== ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    read_video(r"C:\Users\Pc\Downloads\WhatsApp Video 2024-09-18 at 19.25.18.mp4")