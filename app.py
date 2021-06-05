import time
import datetime
import cv2
from mss import mss

# Caclulate video lenght and recording time to get wait time between each image capture
recordingLength = 1 * 60*60 # Input in hours
outputVideoFrameRate = 24
outputVideoLength = 0.10 *60 # Input in minutes
captureWait =  round(recordingLength/outputVideoFrameRate/outputVideoLength)
now = datetime.datetime.now()
recordingStopTime = now+datetime.timedelta(seconds=recordingLength)

# Get wait time between photos



print("Sleeptime: ", captureWait)
while datetime.datetime.now() != recordingStopTime:
    print("...")
    time.sleep(captureWait)

    # Set name for file

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    camImageName = f"cam_{now}.png"
    scrImageName = f"scr_{now}.png"
    outputFolder = "data/"


    # Capture Webcam
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1) 
    return_value, image = camera.read()
    cv2.imwrite(outputFolder+camImageName, image)
    del(camera)  # so that others can use the camera as soon as possible
    # print("Camera captured")


    # Capture Screen
    # screenshot = pyautogui.screenshot()
    # screenshot.save(scrImageName)
    # print("Screenshot captured")

    with mss() as sct:
        screenshot = sct.shot(output=outputFolder+scrImageName)












