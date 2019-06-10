# -*- coding: utf-8 -*-
"""
Created on Tue May 22 23:05:39 2018
@author: Abhijeet Kumar
"""

import time
import sys
import os
import subprocess

#import time

os.environ['OMP_THREAD_LIMIT'] = '1'

def convertStandardFormat(img_path):
    
    out_path = str(int(round(time.time() * 1000))) + ".tiff";
    cmd = 'convert -density 300 {0} -depth 8 -strip -background white -alpha off {1}'.format(img_path,out_path)    
    try:
        p = subprocess.Popen(cmd.split(),stderr=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
        output, err = p.communicate()

        if p.returncode:
            raise RuntimeError('ImageMagick returned non-zero status: {}'.format(err))

    except OSError as e:
        raise OSError('Convert not found, install it: ', e)
    
    if os.path.isfile(out_path):
        #img = cv2.imread(out_path)
        return out_path
    
def cleanTextinImage(std_img_path):
    
    out_path = "clean.tiff";
    cmd = ["C://Program Files//Git//bin//sh.exe","--login","-i", "-c",
           "C://Users//acer//Desktop//Abhijeet//OCR//build-ITTRS-Desktop_Qt_5_9_0_MinGW_32bit-Debug//run {} {}".format(std_img_path,out_path)]    
    try:
        p = subprocess.Popen(cmd,stderr=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
        output, err = p.communicate()

        if p.returncode:
            raise RuntimeError('Text_cleaner returned non-zero status: {}'.format(err))

    except OSError as e:
        raise OSError('Text_cleaner not found, install it: ', e)
    
    if os.path.isfile(out_path):
        return out_path
    

def main():
    path = sys.argv[1]
    #path = "./test/licenseplate.png"
    img_path = convertStandardFormat(path)
    cleanTextinImage(img_path)
    
if __name__ == '__main__':
    main()
    