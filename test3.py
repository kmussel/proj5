import os
import time

print("Executing Numero 3", flush=True)

time.sleep(10)

print("Numero 3: More")
print(os.environ, flush=True)
cnt = 0
while cnt < 7:
    print("IN LOOP {}".format(cnt), flush=True)
    time.sleep(2)
    cnt += 1


print("Numero 3: DONE")