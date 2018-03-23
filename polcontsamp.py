import os
import time


while 1:
    os.system("date")
    print("getmany -v2c -timeout 70 1.1.1.1 public ospf")
    os.system("getmany -v2c -timeout 70 1.1.1.1 public ospf")
    os.system("date")
    print("1800s sleep Half an Hour")
    time.sleep(1800)
