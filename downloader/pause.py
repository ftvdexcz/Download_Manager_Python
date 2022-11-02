import threading
import random
import time
import requests
import urllib.request
import shutil
import sys

def download():
  global pause
  # url = 'http://212.183.159.230/100MB.zip'
  url = 'https://getsamplefiles.com/download/rar/sample.rar'
  req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  # req.headers['Range'] = f'bytes={0-5242}'
  # 12895 bytes
  
  blocksize = 1
  res = urllib.request.urlopen(req) 

  with open('downloads/part', 'wb') as f:
    while True:
      if pause:
        print('pause')
        continue
      print('downloading...')
      try:
        buff = res.read(blocksize)  
      except Exception as e:
        raise

      if not buff:
        break
      
      f.write(buff)
  print('Done')


pause = False

thread = threading.Thread(target=download)
thread.start()

while True:
  if pause == 'Done':
    break
  tmp = input()
  pause = tmp