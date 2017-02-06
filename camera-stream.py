import picamera
import time
from time import strftime
from sense_hat import SenseHat
import json

sense = SenseHat()
sense.set_imu_config(True, True, True)

record_time = 5
device_ID = "nd001"
camera_ID = "nc001"
camera_TP = "IP"
curr_time = strftime ("%Y_%m_%d_%H:%M:%S")
'''
def write_to_file():
    time_start = strftime ("%Y_%m_%d_%H:%M:%S" + ".h264")
    time_start_2 = strftime ("%H:%M:%S")
    camera.start_recording(str(time_start))
    camera.start_preview()
    
    data = {
        "date      ": strftime ("%Y-%m-%d"),
        "deviceID  ": device_ID,
        "cameraID  ": camera_ID,
        "cameraTP  ": camera_TP,
        "time_begin": time_start_2
        }
        
def sensors_data_to_file():    
    for i in range(record_time):
        orientation_rad = sense.get_orientation_radians()
        d = ("{pitch}".format(**orientation_rad), "{roll}".format(**orientation_rad), "{yaw}".format(**orientation_rad))
        curr_time = strftime ("%H:%M:%S")
        d_f_sens = {
                    "time" : curr_time,
                    "pitch" : d[0],
                    "roll" : d[1],
                    "yaw" : d[2]
                    }
        print (d_f_sens)
        file.write(json.dumps(d_f_sens, indent = 4))
        time.sleep(1)
'''        
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    time_start = strftime ("%Y_%m_%d_%H:%M:%S" + ".h264")
    time_start_2 = strftime ("%H:%M:%S")

    data = {
        "date      ": strftime ("%Y-%m-%d"),
        "deviceID  ": device_ID,
        "cameraID  ": camera_ID,
        "cameraTP  ": camera_TP,
        "time_begin": time_start_2,
        "time_end  ": time_start_2
    }
    file_name = 'pos:{0}_dev:{1}_cam:{2}.json'.format(strftime ("%Y-%m-%d"), device_ID, camera_ID)
    
    with open(str(file_name), mode='a', encoding='utf-8')  as file:
        orientation_rad = sense.get_orientation_radians()
        camera.start_recording(str(time_start))
        camera.start_preview()
            
        for i in range(record_time):
            orientation_rad = sense.get_orientation_radians()
            d = ("{pitch}".format(**orientation_rad), "{roll}".format(**orientation_rad), "{yaw}".format(**orientation_rad))
            curr_time = strftime ("%H:%M:%S")
            d_f_sens = {
                    "time" : curr_time,
                    "pitch" : d[0],
                    "roll" : d[1],
                    "yaw" : d[2]
                    }
            print (d_f_sens)
            file.write(json.dumps(d_f_sens, indent = 4, sort_keys=True))
            time.sleep(1)
            
        camera.stop_recording()
        print("recorded")
        time_end = strftime ("%H:%M:%S")
        data = {
        "date      ": strftime ("%Y-%m-%d"),
        "deviceID  ": device_ID,
        "cameraID  ": camera_ID,
        "cameraTP  ": camera_TP,
        "time_begin": time_start_2,
        "time_end  ": time_end 
            }
        file.write(json.dumps(data, indent = 2, sort_keys=True))
        file.close()
    
exit(True)
