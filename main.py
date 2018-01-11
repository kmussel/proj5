from skafossdk import Skafos
import logging

# comment

def hello_world():
  print("Hello, world.")
  skafos = Skafos(log_level=logging.DEBUG)

if __name__ == "__main__":
  hello_world()
