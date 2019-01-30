import sys
import cv2
from datetime import datetime

vid_cap = None
frame = None

def log(message):
    print(datetime.now(), 'LOG::', message)

def error(message):
    print(datetime.now(), 'ERROR::', message)

def trackbar_callback(arg):
    log('trackbar_callback: {}'.format(arg))
    show_frame(arg)

def read_frame(frame_no):
    global frame
    vid_cap.set(1, frame_no)
    ret, frame = vid_cap.read()
    if not ret:
        exit(0)

def show_frame(frame_no):
    global frame
    read_frame(frame_no)
    cv2.imshow('frame', frame);
    k = cv2.waitKey(0)
    log('Pressed "{}"'.format(k))
    if k == ord('q'):
        exit(0)
    cv2.setTrackbarPos('frame#', 'frame', frame_no+1)

def main(video_filename):
    global vid_cap

    vid_cap = cv2.VideoCapture(video_filename)
    if vid_cap.isOpened():
        log('Video file loaded.')
    vid_len = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cv2.namedWindow('frame')
    cv2.createTrackbar('frame#','frame', 0, vid_len-1, trackbar_callback)

    show_frame(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        error('Please provide filename')
        exit(1)
    filename = sys.argv[1]

    main(filename)
