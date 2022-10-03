import cv2
import glob
import os

folder = glob.glob("D:\\Mianwali AI\\Ciggrette Waste Detection AI\\videos")

video_list = []
for i in folder:
    for j in glob.glob(i + "\\*.mp4"):
        video_list.append(j)
        # print(j)
# pathIn = video_list
pathOut = "D:\\Mianwali AI\\Ciggrette Waste Detection AI\\multi_path"
frame_number = 0
def extractImages(pathIn, pathOut):
    global frame_number
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    # finding video length===================================
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    video_length = round(frames / fps)
    print("=============================")
    print("Video Length: ", video_length)
    print("=============================")
    # calculate duration of the video========================
    success,image = vidcap.read()
    success = True
    vid_len = (video_length*2)+2
    print("=============================")
    print("Video Length: ", vid_len)
    print("=============================")
    while success and count!=vid_len-4:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))    # added this line
        # print(vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))) 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        cv2.imwrite( pathOut + "//frame%d.jpg" % frame_number, image)     # save frame as JPEG file
        count = count + 1
        frame_number = frame_number + 1
    print("===========Function Ended=============")

# count = 0
for i in video_list:
    print(f"Entering the function for {i}th video")
    # video_frames = i.get(cv2.CAP_PROP_FRAME_COUNT)
    # video_fps = i.get(cv2.CAP_PROP_FPS)
    # calculate duration of the video
    # video_len= round(video_frames / video_fps)
    # print("Video Length: ", video_len)
    extractImages(i, pathOut)
    print("Exiting Function")
# extractImages(pathIn, pathOut)