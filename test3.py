import os
import time

print("Executing Numero 3", flush=True)

time.sleep(10)

print("Numero 3: SOME MORE")

cnt = 0
while cnt < 7:
    print("IN LOOP {}".format(cnt), flush=True)
    time.sleep(10)
    cnt += 1


print("Numero 3: DONE")