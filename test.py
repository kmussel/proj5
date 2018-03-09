import os
import time
import sys
#import conda
#from subprocess import call

#call(["conda", "install", "-y", "pytorch-cpu", "torchvision", "-c", "maciejkula", "-c", "pytorch", "spotlight"])

# conda install -y pytorch-cpu torchvision -c maciejkula -c pytorch spotlight

def main():
    print("HELLO test.py")

    # os.environ["TESTING"] = "123"    
    print(os.environ, flush=True)
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