from sense_hat import SenseHat
import time
from time import strftime
import json

sense = SenseHat()
sense.set_imu_config(False, True, False)
with open('1.txt', mode='w', encoding='utf-8')  as file:
    i = 5
    for i in range(i):
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
    file.close()

exit(True)
