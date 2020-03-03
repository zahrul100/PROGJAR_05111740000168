import logging
import requests
import threading
from datetime import datetime
import os



def download_gambar(url=None,nama=None):
    if (url is None):
        return False
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = nama
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi},Diunduh pada waktu = {current_time} ")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':

    threads = []

    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg','1',))
    threads.append(t)
    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/QmwetR03O1pyroXV74IgbXXLF74=/0x156:2000x1156/780x390/data/photo/2020/03/02/5e5ca809a8b00.jpg','2',))
    threads.append(t)
    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/CJ7twPr3FXwj2vlhEzVl-jDABws=/0x41:1000x708/750x500/data/photo/2020/03/01/5e5b66c42d2f1.jpg','3',))
    threads.append(t)
    for thr in threads:
        thr.start()
  #  download_gambar('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')
