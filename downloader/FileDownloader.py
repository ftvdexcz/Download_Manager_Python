from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import requests
from downloader.download_part_multithread import Downloader

class Progress:
    def __init__(self, window):
      self.window = window

    def __call__(self, blocknum, blocksize, totalsize):
      readedData = blocknum * blocksize
      if totalsize > 0:
        downloadPercentage = readedData * 100 / totalsize
        self.window.progressBar.setValue(downloadPercentage)
        QApplication.processEvents() # pending events to process

class FileDownloader:
  @staticmethod
  def choose_save_location(window):
    try:
      saveLocation = QFileDialog.getSaveFileName(window, caption='Save as', directory='.', filter='All Files(*.*)')

      window.lineEdit_2.setText(saveLocation[0])
    except:
      print('error')

  @staticmethod
  def download(window):
    print('downloading...')

    downloadUrl = window.lineEdit.text()
    saveLocation = window.lineEdit_2.text()
    print(downloadUrl)
    if downloadUrl == '' or saveLocation == '':
      QMessageBox.warning(window, 'Data Error', 'URL hoặc save location không hợp lệ')
      return
    
    try:
      opener = urllib.request.build_opener()
      opener.addheaders = [('User-agent', 'Mozilla/5.0')] # Thêm header cho lỗi 403 
      urllib.request.install_opener(opener)
      urllib.request.urlretrieve(downloadUrl, saveLocation, Progress(window))
    except Exception as e:
      QMessageBox.warning(window, 'Download Error', 'Download không thành công')
      return 
    window.progressBar.setValue(100)
    QMessageBox.information(window, 'Tải thành công', 'Tải xuống thành công!')

    # Reset
    window.lineEdit.setText('')
    window.lineEdit_2.setText('')
    window.progressBar.setValue(0)

  @staticmethod
  def download2(window, numThreads, blocksize, pause):
    '''update download đa luồng: xóa progressbar'''
    window.textEdit.setText('')

    downloadUrl = window.lineEdit.text()
    saveLocation = window.lineEdit_2.text()
    
    if downloadUrl == '' or saveLocation == '':
      QMessageBox.warning(window, 'Data Error', 'URL hoặc save location không hợp lệ')
      return

    print('downloading...')
    
    d = Downloader(downloadUrl, numThreads, blocksize, pause, saveLocation, window)
    
    d.start_download()
    
    # Reset
    window.lineEdit.setText('')
    window.lineEdit_2.setText('')

  @staticmethod 
  def pause_download(window, pause):
    '''pause/resume download'''
    boolean = pause[0]

    if boolean == True: # đang tạm dừng
      pause[0] = False
      window.pushButton_14.setText('Tiếp tục')
    else: # đang tải
      pause[0] = True
      window.pushButton_14.setText('Tạm dừng')
