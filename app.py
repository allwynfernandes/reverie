
import os
import shutil
import time
import datetime
import cv2
from mss import mss
from movie import make_montage

# Accept inputs

recordingLength =  int(input("How long do you want to record?(hours): ") or 3)* 60*60 # Input in hours
outputVideoFrameRate = int(input("Output video framerate? (Default:21 ): ") or 21)
outputVideoLength = int(float(input("Length of final movie [0.1 to 0.9]: ") or 0.5) *60) # Input in minutes




# Caclulate video lenght and recording time to get wait time between each image capture

# recordingLength = 9 * 60*60 # Input in hours
# outputVideoFrameRate = 24 # 24fps ~= 175BPM for the bg audio
# outputVideoLength = 1 *60 # Input in minutes. Ideal value is 5% of recordingLength


captureWait =  round(recordingLength/outputVideoFrameRate/outputVideoLength)
now = datetime.datetime.now()
recordingStopTime = now+datetime.timedelta(seconds=recordingLength)

scrOutputFolder = "data/scr/"
camOutputFolder = "data/cam/"
camVidSize = 120
# Get wait time between photos

def reset_folder(path):
    for i in path:
        shutil.rmtree(i)
        os.makedirs(i)


print("Sleeptime: ", captureWait)


def main():
    while datetime.datetime.now() <= recordingStopTime:
        print("...")
        time.sleep(captureWait)

        # Set name for file

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        scrImageName = f"scr_{now}.png"
        camImageName = f"cam_{now}.png"

        # Capture Screen
        with mss() as sct:
            screenshot = sct.shot(output=scrOutputFolder+scrImageName)

        # Capture Webcam
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(0.1) 
        return_value, image = camera.read()
        cv2.imwrite(camOutputFolder+camImageName, image)
        del(camera)

    make_montage(camVidSize, outputVideoFrameRate, useSubClip=True)
    reset_folder([scrOutputFolder, camOutputFolder])


if __name__ == '__main__':
    main()










