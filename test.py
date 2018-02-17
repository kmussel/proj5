import os
import time

print("HELLO")

time.sleep(10)

print("SOME MORE")

#time.sleep(10)
cnt = 0
while cnt < 20:
    print("IN TEST1 LOOP {}".format(cnt), flush=True)
    time.sleep(10)
    cnt += 1

print("DONE")