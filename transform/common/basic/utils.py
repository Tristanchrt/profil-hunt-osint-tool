import cv2
from urllib.request import urlopen
import numpy as np

def url_to_img(url):
    req = urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    return cv2.imdecode(arr, -1)
