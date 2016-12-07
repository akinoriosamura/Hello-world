#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Extract QRcode location from drone.
"""

import zbar
from PIL import Image
import time

start = time.time()

for i in range(10):
    input_path = "center.jpg"

    # create a reader
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('enable')

    # obtain image data
    pil = Image.open(input_path).convert('L')
    (width, height) = pil.size
    raw = pil.tostring()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    for symbol in image:
        # extract location
        loc = symbol.location[0]
        print(symbol.data)

    print(loc)
    del(image)

elapsed_time = time.time() - start

print ("ave_elapsed_time:{0}".format(elapsed_time/10)) + "[sec]"