import picamera
import time
import datetime as dt
from time import strftime

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    
    camera.start_recording('timestamped.h264')
    file = open("time.txt", "a")
    s = strftime ("%a, %d %b %Y %H:%M:%S")
    file.write ("video_start ")
    file.write (str(s))
    file.write ('\n')
    camera.wait_recording(5)
    camera.stop_recording()
    t = strftime ("%a, %d %b %Y %H:%M:%S")
    file.write ("video_stop  ")
    file.write (str(t))
    file.write ('\n')
    file.close()
    print("recorded")
       
