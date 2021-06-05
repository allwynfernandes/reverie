
# Init variables
recordingLength = 3 #2 * 60*60 # Input in hours
outputVideoFrameRate = 24
outputVideoLength = 0.5 *60 # Input in minutes

# Get wait time between photos
captureWait = recordingLength/outputVideoFrameRate/outputVideoLength



print("Capture Wait: ", round(captureWait),"\n","Capture Length: ",recordingLength/60/60)

import datetime

now = datetime.datetime.now()
print("Recording started: ", now)

recordingStopTime = now+datetime.timedelta(seconds=recordingLength)

while datetime.datetime.now() != recordingStopTime:
    print("Live")

print("Stoped: ", recordingStopTime)
