import cv2
from camera_service.modules.start_modules import start_processing

def cam_capture():
    cap = cv2.VideoCapture(0)  # 0 for default webcam, change if necessary
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_number += 1

        start_processing(frame, frame_number)
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam_capture()