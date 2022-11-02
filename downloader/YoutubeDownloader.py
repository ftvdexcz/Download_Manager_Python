from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pafy
import humanize
import os
import os.path
# import youtube_dl
# from pytube import Playlist

pafy.set_api_key('AIzaSyDAeZgCfL0vcZEvyDKnwBvnR9buakJMc4M')

class VideoProgress:
  def __init__(self, window):
    self.window = window

  def __call__(self, totalsize, received, ratio, rate, time):
    readedData = received
    if totalsize > 0:
      downloadPercentage = readedData * 100 / totalsize
      self.window.progressBar_2.setValue(downloadPercentage)
      
      if time < 60: 
        self.window.label_5.setText('{} seconds remaining'.format(time))
      elif time < 60*60: 
        self.window.label_5.setText('{} minutes remaining'.format(time//60))
      else:
        self.window.label_5.setText('{} hours remaining'.format(time//3600))

      QApplication.processEvents()

class PlaylistProgress:
  def __init__(self, window):
    self.window = window

  def __call__(self, totalsize, received, ratio, rate, time):
    readedData = received
    if totalsize > 0:
      downloadPercentage = readedData * 100 / totalsize
      self.window.progressBar_3.setValue(downloadPercentage)
      
      if time < 60: 
        self.window.label_6.setText('{} seconds remaining'.format(time))
      elif time < 60*60: 
        self.window.label_6.setText('{} minutes remaining'.format(time//60))
      else:
        self.window.label_6.setText('{} hours remaining'.format(time//3600))

      QApplication.processEvents()

class YoutubeDownloader:
  @staticmethod
  def choose_save_location_video(window):
    try:
      saveLocation = QFileDialog.getSaveFileName(window, caption='Save as', directory='.', filter='All Files(*.*)')

      window.lineEdit_4.setText(saveLocation[0])
    except:
      print('e')

  @staticmethod
  def get_video_info(window): 
    videoUrl = window.lineEdit_3.text()

    if videoUrl == '':
      QMessageBox.warning(window, 'URL Error', 'URL không hợp lệ')
      return

    try:
      print(videoUrl)
      video = pafy.new(videoUrl)
      print(video.title)
      print(video.duration)

      videoStreams = video.videostreams
      for stream in videoStreams:
        size = humanize.naturalsize(stream.get_filesize()) 
        data = '{} {} {} {}'.format(stream.mediatype, stream.extension, stream.quality, size)
        window.comboBox.addItem(data)
    except Exception as e:
      print(e)
      return

  @staticmethod
  def download_video(window):
    videoUrl = window.lineEdit_3.text()
    saveLocation = window.lineEdit_4.text()

    if videoUrl == '' or saveLocation == '':
      QMessageBox.warning(window, 'Data Error', 'URL hoặc Location không hợp lệ')
      return 
    
    try:
      video = pafy.new(videoUrl)
      # bestaudio = video.getbestaudio()
      # bestaudio.download()
      videoStream = video.videostreams
      videoQuality = window.comboBox.currentIndex()
      download = videoStream[videoQuality].download(filepath=saveLocation, callback=VideoProgress(window))
    except Exception as e:
      print(e)
      return
    
    QMessageBox.information(window, 'Tải thành công', 'Tải xuống thành công!')

    # Reset
    window.lineEdit_3.setText('')
    window.lineEdit_4.setText('')
    window.progressBar_2.setValue(0)
    window.label_5.setText ('')
    window.comboBox.clear()

  @staticmethod
  def choose_save_location_playlist(window):
    saveLocation = QFileDialog.getExistingDirectory(window, 'Select Download Directory')
    window.lineEdit_6.setText(saveLocation)

  @staticmethod
  def download_playlist(window):
    playlistUrl = window.lineEdit_5.text()
    saveLocation = window.lineEdit_6.text()

    if playlistUrl == '' or saveLocation == '':
      QMessageBox.warning(window, 'Data Error', 'URL hoặc Location không hợp lệ')
      return 
    
      # ydl_opts= {}
      # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      #   playlistVideos = ydl.extract_info(playlistUrl, download=False)
      #   print(playlistVideos)   
    # try:
    playlistVideos = pafy.get_playlist2(playlistUrl)
    window.lcdNumber_2.display(len(playlistVideos))
    title = playlistVideos.title
    print(title)

    os.chdir(saveLocation)
    if os.path.exists(title):
      os.chdir(title)
    else:
      os.mkdir(title)
      os.chdir(title)
    
    currentVideo = 1 
    quality = window.comboBox_2.currentIndex()
    QApplication.processEvents()

    for video in playlistVideos:
      try:
        window.lcdNumber.display(currentVideo)
        cur_stream = video.videostreams
        print(quality)
        download = cur_stream[quality].download(callback=PlaylistProgress(window))
        QApplication.processEvents()

        currentVideo += 1
      except Exception as e:
        print(e)
        return