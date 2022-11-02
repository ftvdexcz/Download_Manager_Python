import keyboard
import threading

class PauseHandlerWorkers(threading.Thread):
  def __init__(self, window, pause, **kwargs):
    super(PauseHandlerWorkers, self).__init__(**kwargs)
    self.window = window
    self.pause = pause
    self.start()

  def run(self):
    while True:
      try:
        keyboard.wait('p')
        '''pause/resume download'''
        boolean = self.pause[0]

        if boolean == True: # đang tạm dừng
          self.pause[0] = False
          print('resume')
        else: # đang tải
          self.pause[0] = True
          print('pause')
      except Exception as e:
        print(e)

