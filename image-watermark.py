#!/usr/bin/python
######################################################
### (c) Copyright by Giovambattista Vieri 2022
### All Rights Reserved
### License AGPL V 3.0
### Software status ALPHA. This software is an experiment.
### Run it if you dare. No guarantee at all. 
######################################################


import sys
import cv2
import argparse
import numpy as np
from datetime import date
from pprint import pprint


def getOptions(args=sys.argv[1:]):
    parser=argparse.ArgumentParser(description='This simple program will help you to watermark an image')
    parser.add_argument('-i','--imagename', help='image file name', action='store', dest="imagefilename", required=True )
    parser.add_argument('-m','--message', help='message to be watermark (you can use "" to insert more words', action='store',default='',  dest='message' )
    parser.add_argument('-f','--font', help='font', action='store',default='0',  dest='font', choices=['0','1','2','3','4','5','6','7'] )
    parser.add_argument('-a','--alpha', help='alpha (transparency) ', action='store',default='0.3',  dest='alpha', type=float )
    parser.add_argument('-v','--verbose', help='more verbose output', action='store_true')
    opt=parser.parse_args(args)
    return(opt)


##########################################
if __name__ == "__main__":
    today = date.today()
    opt=getOptions()
    verbose=opt.verbose

    if(verbose):
        pprint(opt)

    # Read in the image
    image_file = opt.imagefilename
    image = cv2.imread(image_file)
    #overlay = image.copy()
    output = image.copy()
    height, width, channels = image.shape
    if (verbose):
        print ("height   : = ",height)
        print ("width    : = ",width)
        print ("channels : = ",channels)
    overlay =  np.zeros((height, width, channels), dtype=np.uint8)




# Stamp the message on image lower right corner 
    cv2.putText(overlay, str(today), (int(width/10),int (height/8)), int(opt.font), 2.5, (255,255,255), thickness=2)
    cv2.putText(overlay, opt.message, (int(width/10),int (height/8*7)), cv2.FONT_HERSHEY_PLAIN, 2.5, (255,255,255), thickness=2)
    if(verbose):
        cv2.imshow("overlay",overlay)
    cv2.addWeighted(overlay, opt.alpha, output, 1 - opt.alpha, 0, output)
    if(verbose):
        cv2.imshow("output",output)
# Save the image    
    cv2.imwrite(opt.imagefilename+".out.jpg", output)
    if(verbose):
        cv2.waitKey(15000)
