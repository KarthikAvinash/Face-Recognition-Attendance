import cv2
import os
from tqdm import tqdm

def FrameCapture(video_path, output_dir, frame_period):
    vidObj = cv2.VideoCapture(video_path)
    total_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    count = 0
    pbar = tqdm(total=total_frames // frame_period, desc="Extracting frames", unit="frame")
    success = 1
    while success:
        success, image = vidObj.read()
        if success:
            if count % frame_period == 0:
                os.makedirs(output_dir, exist_ok=True)
                frame_path = os.path.join(output_dir, "frame%d.jpg" % (count // frame_period))
                cv2.imwrite(frame_path, image)
                pbar.update(1)
        count += 1
    pbar.close()

# INPUT_________________________________________________________________________________
videos_folder = "C:\\Face recognition attendance\\Videos"
frame_period = 5
#________________________________________________________________________________________

for root, dirs, files in os.walk(videos_folder):
    for video_file in files:
        if video_file.endswith(".MOV"):
            video_path = os.path.join(root, video_file)
            video_base_name = os.path.splitext(video_file)[0]
            video_subdir = os.path.join(root, video_base_name)
            FrameCapture(video_path, video_subdir, frame_period)

