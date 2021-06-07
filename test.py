
# Init variables

recordingLength =  int(input("How long do you want to record?(hours): ") or 3)* 60*60 # Input in hours
outputVideoFrameRate = int(input("Output video framerate? (Default:21 ): ") or 21)
outputVideoLength = int(float(input("Length of final movie [0.1 to 0.9]: ") or 0.5) *60) # Input in minutes

print("Capture Length: ",recordingLength/60/60, "Framerate", outputVideoFrameRate, "Vid length", outputVideoLength)


# Get wait time between photos
# captureWait = recordingLength/outputVideoFrameRate/outputVideoLength



# print("Capture Wait: ", round(captureWait),"\n","Capture Length: ",recordingLength/60/60, "Framerate", outputVideoFrameRate)

import datetime

now = datetime.datetime.now()
print("Recording started: ", now)

recordingStopTime = now+datetime.timedelta(seconds=recordingLength)

# while datetime.datetime.now() != recordingStopTime:
#     print("Live")

# print("Stoped: ", recordingStopTime)
