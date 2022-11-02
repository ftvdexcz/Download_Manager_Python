from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import getopt


def append_log(window, msg):
    window.textEdit.append(msg)

def downloadfile_multithread(window):
  pass

def parse_args(argv):
  try:
    # t: number_of_threads
    options, args = getopt.getopt(argv, "t:b:",
                               ["threads=",
                                "blocksize="])

    opt = {}
    for k, v in options: 
      opt[k] = v
    return opt 
                   
  except:
    print("Error Message ")

if __name__ == '__main__':
  pass