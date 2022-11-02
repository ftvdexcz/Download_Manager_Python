import pyperclip
import threading
import time
import requests
import pafy

class ClipboardWorkers(threading.Thread):
  def __init__(self, window, **kwargs):
    super(ClipboardWorkers, self).__init__(**kwargs)
    self.window = window
    self.start()

  def run(self):
    while True:
      s = pyperclip.waitForNewPaste()
      # self.lst.append(s)
      try:
        headers = requests.head(s).headers
        downloadable = 'attachment' in headers.get('Content-Disposition', '')
        if downloadable:
          print('downloadable: file')
          
          self.window.lineEdit.setText(s)
      except Exception:
        pass

      try:
          video = pafy.new(s)
          print('downloadable: video')
        
          print(video.title)
          self.window.lineEdit_3.setText(s)
      except Exception:
        pass

      try: 
        playlistVideos = pafy.get_playlist2(s)
        
        print('downloadable: playlist')
        print(playlistVideos.title)
        self.window.lineEdit_5.setText(s)
      except Exception:
        pass

def main():
  lst = []
  clipboardWorkers = ClipboardWorkers(lst, daemon=True)

  while True:
    time.sleep(5)
    print(lst)

if __name__ == '__main__':
  main()