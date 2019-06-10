# -*- coding: utf-8 -*-
"""
Created on Tue May 22 23:05:39 2018
@author: Abhijeet Kumar
"""

import pytesseract
import time
import cv2
import numpy as np
import sys
import os
import re
import glob
import concurrent.futures 
import subprocess

#import time

os.environ['OMP_THREAD_LIMIT'] = '1'

def convertStandardFormat(img_path):
    
    out_path = "etc//" + str(int(round(time.time() * 1000))) + ".tiff";
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
    
    out_path = "etc//" + str(int(round(time.time() * 1000))) + ".tiff";
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
        cleaned_img = cv2.imread(out_path)
        return cleaned_img
    
    
def removeBorders(img):
    edges = cv2.Canny(img,75,200,apertureSize = 3)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,200,900,100)
    
    if lines is not None:
        for line in lines:    
            for x1,y1,x2,y2 in line:
                cv2.line(img,(x1,y1),(x2,y2),(255,255,255),4)
    return img

def ocr(img_path):
    out_dir = "ocr_results//"
    std_img_path = convertStandardFormat(img_path)
    img = cv2.imread(std_img_path)
    #img = cleanTextinImage(std_img_path)
    text = pytesseract.image_to_string(img,lang='eng')
    out_file = re.sub(".png",".txt",img_path.split("\\")[-1])
    out_path = out_dir + out_file
    fd = open(out_path,"w")
    fd.write("%s" %text)
    fd.close()
    return out_file

def main():
    path = sys.argv[1]
    #path = "C:\\Users\\wns2kadmin\\Downloads\\build-ITTRS-Desktop_Qt_5_9_0_MinGW_32bit-Release\\build-ITTRS-Desktop_Qt_5_9_0_MinGW_32bit-Debug\\test"    
    if os.path.isdir(path) == 1:
        out_dir = "ocr_results//"
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        file_paths = [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".png")]
        
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            #image_list = map(cv2.imread, glob.glob(path+"\\*.png"))    
            image_list = glob.glob(path+"\\*.png")
            for img_path,out_file in zip(file_paths,executor.map(ocr,image_list)):
                print(img_path.split("\\")[-1],',',out_file,', processed')
                sys.stdout.flush()
                
    else:
        img_path = convertStandardFormat(path)
        #img = cleanTextinImage(img_path)
        img = cv2.imread(img_path)
        #img = removeBorders(img)
        text = pytesseract.image_to_string(img,lang='eng')
        fp = open("./ocr_result.txt","w")
        fp.write("%s" %text)
        fp.close()

if __name__ == '__main__':
    main()
   