import os
import time
import sys


def main():
    print("HELLO")

    os.environ["TESTING"] = "123"
    #print(sys.argv)

    # time.sleep(10)

    print("SOME MORE")

    #time.sleep(10)
    # cnt = 0
    # while cnt < 20:
    #     print("IN TEST1 LOOP {}".format(cnt), flush=True)
    #     time.sleep(10)
    #     cnt += 1

    print("DONE")

    return "MY RETURN DATA"

if __name__ == '__main__':
     main()