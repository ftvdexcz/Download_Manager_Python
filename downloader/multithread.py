import gzip
import os
import sys
import zipfile
import zlib

import requests
import threading
import queue
import urllib.request
import time
import timeit
import math
import shutil

class Item:
    def __init__(self, chunk_id, chunk_range, was_interrupted=False):
        self.chunk_id = chunk_id  # chunk id to be downloaded
        self.chunk_range = chunk_range  # chunk range to download from server
        self.was_interrupted = was_interrupted

class Downloader:
    def __init__(self, url=None, num_threads=1):
        self.url = url
        self.num_threads = num_threads
        self.file_size = self.get_file_size()
        self.if_byte_range = self.is_byte_range_supported()
        self.q = queue.Queue(maxsize=0)
        self.start_time = None
        self.end_time = None
        self.range_list = list()
        self.append_write = 'wb'
        self.download_durations = [None] * self.num_threads
        self.download_status = list()
        self.current_status = ""
        self.status_refresh_rate = 2
        self.target_filename = os.path.basename(self.url)

    def get_url(self):
        """Returns URL of a file to be downloaded"""
        return self.url

    def set_url(self, url):
        """Set new URL of a file to be downloaded
        :param url: string
        """
        if not url:
            raise ValueError("URL field is empty")
        if not isinstance(url, str):
            raise TypeError("URL must be of string type")
        self.url = url

    def get_number_of_threads(self):
        """Returns maximum number of threads allowed"""
        return self.num_threads

    def set_number_of_threads(self, number_of_threads):
        """Set new maximum number of threads allowed (must be a positive number)
        :param number_of_threads: integer
        """
        if number_of_threads <= 0:
            raise ValueError("Number of maximum threads should be positive")
        if not isinstance(number_of_threads, int):
            raise TypeError("Number of maximum threads should be integer")
        self.num_threads = number_of_threads

    def get_file_size(self):
        headers = {'Accept-Encoding': 'identity'}
        self.file_size = requests.head(self.url, headers=headers).headers.get('content-length', None)
        if self.file_size is None:
            return
        return int(self.file_size)

    def is_byte_range_supported(self):
        """Return True if accept-range is supported by the url else False
        :return: boolean
        """
        server_byte_response = requests.head(self.url, headers={'Accept-Encoding': 'identity'}).headers.get(
            'accept-ranges')
        if not server_byte_response or server_byte_response == "none":
            return False
        else:
            return True

    def fill_initial_queue(self):
        i = 0
        chunk_size = int(math.ceil(int(self.file_size) / int(self.num_threads)))
        for _ in range(self.num_threads):
            if (i + chunk_size) < self.file_size:
                entry = '%s-%s' % (i, i + chunk_size - 1)
            else:
                entry = '%s-%s' % (i, self.file_size)
            i += chunk_size
            self.range_list.append(entry)

        for chunk_id, chunk_range in enumerate(self.range_list):
            self.q.put(Item(chunk_id, chunk_range, False))

    def download_chunk(self):
        while True:
            item = self.q.get()
            try:
                if item.was_interrupted:
                    time.sleep(1)
                    if os.path.isfile('temp/part/' + str(item.chunk_id)):
                        self.append_write = 'ab'
                        temp = item.chunk_range.split('-') 
                        item.chunk_range = str(int(temp[0]) + os.stat("temp/part" + str(item.chunk_id)).st_size) + '-' + \
                                           temp[1]  # override chunk_range
                    else:
                        self.append_write = 'wb'

                req = urllib.request.Request(self.get_url(), headers={'User-Agent': 'Mozilla/5.0'})
                req.headers['Range'] = 'bytes={}'.format(item.chunk_range) 
                with urllib.request.urlopen(req) as response, open('temp/part' + str(item.chunk_id),
                                                               self.append_write) as out_file:
                    shutil.copyfileobj(response, out_file)

                self.download_durations[item.chunk_id] = timeit.default_timer()
            except IOError:
                print('error when download part chunk')
                item.was_interrupted = True
                self.q.put(item)  # put item back to queue

            finally:
                self.q.task_done()  # release (q.join())

    def get_status_header(self):
        """Returns header for the download status"""
        status_header = list()
        for i in range(self.num_threads):
            status_header.append("chunk" + str(i + 1))
        return '\t\t'.join(status_header)

    def get_download_status(self):
        """Returns current download status per thread separated by tabs in a string format
        :return: string
        """
        self.download_status.clear()
        for i in range(self.num_threads):
            if os.path.isfile('temp/part' + str(i)):
                self.download_status.append(
                    str(round(os.stat("temp/part" + str(i)).st_size / (self.file_size / self.num_threads) * 100)) + "%")
            else:
                self.download_status.append("0.00%")
        self.current_status = '\t\t'.join(self.download_status)
        if all(x == "100%" for x in self.download_status):
            return False
        else:
            return True

    def start_download(self):
        self.start_time = timeit.default_timer()
        print('Data is compressed? ...', end='')
        if self.file_size is None:
            print('Yes')
            try:
                print("Download file at once ... ", end="")
                self.download_entire_file()

                zipf = zipfile.ZipFile(self.target_filename, 'r')
                zipf.extractall('')

                print("Done")
            except:
                print("Error occurred while downloading.")
        else:
            print('No')
            print("Server support byte range GET? ... ", end="")
            if self.if_byte_range:
                print("Yes")
                if os.path.isdir("temp"):
                    shutil.rmtree("temp")

                os.mkdir('temp')
                self.fill_initial_queue()

                print("Starting download threads ... ", end="")
                for i in range(self.num_threads):
                    worker = threading.Thread(target=self.download_chunk)
                    worker.setDaemon(True)
                    worker.start()
                print("Done")

                print(self.get_status_header())
                while self.get_download_status():
                    print(self.current_status)
                    time.sleep(self.status_refresh_rate)

                self.q.join()
                print(self.current_status)
                print("File chunks download ... Done")
                print("Merging chunks into a single file ... ", end="")

                with open(self.target_filename, "ab") as target_file:
                    for i in range(self.num_threads):
                        with open("temp/part" + str(i), "rb") as chunk_file:
                            target_file.write(chunk_file.read())
                print("Done")
                if os.path.isdir("temp"):
                    shutil.rmtree("temp")
            else:
                print('No')
                try:
                    print("Download file at once ... ", end="")
                    self.download_entire_file()
                    print("Done")
                except:
                    print("Error occurred while downloading.")

        self.end_time = timeit.default_timer()
        print("Displaying benchmarks ... ")
        self.display_benchmarks()

    def download_entire_file(self):
        r = requests.get(self.url, stream=True)
        with open(self.target_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def display_benchmarks(self):
        """Disply benchmark results"""
        print("\nBenchmarking Results:")
        print("\nTotal time taken for download:", round(self.end_time - self.start_time, 2),
              "seconds.")
        if self.if_byte_range:
            print("\nThread\t\tTime Taken\t\tAverage Download Speed")
            for i in range(self.num_threads):
                total_time = self.download_durations[i] - self.start_time
                average_speed = ((self.file_size / self.num_threads) / total_time) * (8 / (1024 * 1024))
                print(i + 1, "\t\t", round(total_time, 2), "seconds\t\t", round(average_speed, 2), "mbps")


if __name__ == '__main__':
    # 1. test support range
    '''
    url = 'https://figshare.com/ndownloader/files/9491434'
    url2 = 'https://getsamplefiles.com/download/rar/sample.rar'
    url3 = 'https://file-examples.com/wp-content/uploads/2017/02/zip_2MB.zip'
    headers = {'Range': 'bytes=%s-%s' % (0, 1000)}
    req = requests.get(url3)
    print(req.headers)
    print(req.headers.get('Accept-Ranges')) # bytes | none
    '''
    url2 = 'https://getsamplefiles.com/download/rar/sample.rar'
    url3 = 'https://filesamples.com/samples/document/docx/sample4.docx'
    d = Downloader(url2, 2)
    d.start_download()
    # r = requests.get(url3)
    # print(r.headers)
    # print(r.content)


    # headers = {'Accept-Encoding': 'identity'}
    # file_size = requests.head(url3, headers=headers).headers.get('content-length', None)
    # print(file_size)

    # try:
    #     req = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
    #     req.headers['Range'] = 'bytes={}'.format(0-500)
    #     with urllib.request.urlopen(req) as response, open('temp/part' + str(1),
    #                                                        'wb') as out_file:
    #         print(response)
    #         shutil.copyfileobj(response, out_file)
    # except IOError:
    #     print('error')

    # headers = {'Range': 'bytes=0-500'}
    # req = requests.get(url2)
    # print(req.status_code)
    # print(req.headers)



# 12895
# 2 threads: chunk_size = 6448 -> 0-6447, 6448-12895 (size: 6448, 6447)
#

# str(round(os.stat("temp/part" + str(i)).st_size / (self.file_size / self.num_threads) * 100,
#                               2)) + "%")
# print(round(6448/6447.5*100))




