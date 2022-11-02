from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os
import os.path
import utils
import getopt

from downloader.FileDownloader import FileDownloader
from downloader.YoutubeDownloader import YoutubeDownloader
from workers.ClipboardWorkers import ClipboardWorkers
from workers.PauseHandlerWorkers import PauseHandlerWorkers

ui,_ = loadUiType('assets/UI/Download.ui')
num_threads = 1
blocksize = 1024
pause = [False]

class MainApp(QMainWindow, ui):
  def __init__(self, parent=None):
    super(MainApp, self).__init__(parent)
    QMainWindow.__init__(self)
    self.setupUi(self)
    self.initUI()
    self.handleBtn()

  def initUI(self):
    # self.tabWidget.tabBar().setVisible(False)
    self.darkorangeStyle()
    
  def handleBtn(self):
    # self = window
    self.pushButton.clicked.connect(lambda: FileDownloader.download2(self, num_threads, blocksize, pause))
    self.pushButton_2.clicked.connect(lambda: FileDownloader.choose_save_location(self))
    self.pushButton_3.clicked.connect(lambda: YoutubeDownloader.choose_save_location_video(self))
    self.pushButton_4.clicked.connect(lambda: YoutubeDownloader.download_video(self))
    self.pushButton_5.clicked.connect(lambda: YoutubeDownloader.get_video_info(self))
    self.pushButton_6.clicked.connect(lambda: YoutubeDownloader.choose_save_location_playlist(self))
    self.pushButton_7.clicked.connect(lambda: YoutubeDownloader.download_playlist(self))

    self.pushButton_8.clicked.connect(self.openHome)
    self.pushButton_9.clicked.connect(self.openDownload)
    self.pushButton_10.clicked.connect(self.openYoutube)
    self.pushButton_11.clicked.connect(self.openSetting)
    self.pushButton_12.clicked.connect(self.darkorangeStyle)
    self.pushButton_13.clicked.connect(self.qdarkStyle)
    self.pushButton_14.clicked.connect(lambda: FileDownloader.pause_download(self, pause))
    self.pushButton_15.clicked.connect(self.darkbluStyle)
    
  # Change UI
  def openHome(self):
    self.tabWidget.setCurrentIndex(0)

  def openDownload(self):
    self.tabWidget.setCurrentIndex(1)

  def openYoutube(self):
    self.tabWidget.setCurrentIndex(2)

  def openSetting(self):
    self.tabWidget.setCurrentIndex(3)

  def darkorangeStyle(self):
    style = open(r'assets/themes/darkorange.css')
    style = style.read()
    self.setStyleSheet(style)

  def qdarkStyle(self):
    style = open(r'assets/themes/qdark.css')
    style = style.read()
    self.setStyleSheet(style)

  def darkbluStyle(self):
    style = open(r'assets/themes/darkblu.css')
    style = style.read()
    self.setStyleSheet(style)


def main():
  global num_threads
  global blocksize
  opts = utils.parse_args(sys.argv[1:])
  # print(opts)
  if '-t' in opts:
    num_threads = int(opts['-t'])
  elif '--threads' in opts:
    num_threads = int(opts['--threads'])

  if '-b' in opts:
    blocksize = int(opts['-b'])
  elif '--blocksize' in opts:
    blocksize = int(opts['--blocksize'])

  print(f'threads: {num_threads}')
  print(f'blocksize: {blocksize}')

  app = QApplication(sys.argv) # create an application object of QApplication
  window = MainApp()

  clipboardWorkers = ClipboardWorkers(window, daemon=True) # start clipboard thread
  pauseHandlerWorkers = PauseHandlerWorkers(window, pause, daemon=True) 
  window.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()