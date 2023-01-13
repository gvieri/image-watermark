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
    parser=argparse.ArgumentParser(description='This simple program will help you to watermark an image. The -i parameter is the image file name. This name will be added of a ".out." between the file name and the extension. The resulting name will be used for the output file.',epilog='Example of use:')
    parser.add_argument('-i','--imagename', help='image file name', action='store', dest="imagefilename", required=True )
    parser.add_argument('-m','--message', help='message to be watermark (you can use "" to insert more words', action='store',default='',  dest='message' )
    parser.add_argument('-f','--font', help='font', action='store',default='0',  dest='font', choices=['0','1','2','3','4','5','6','7'] )
    parser.add_argument('-d','--dateformat', help='dateformat 0 for 12 Jun, 2018, 1 for 2018-06-12, 2 for 06/12/2018', action='store',default='0',  dest='dateformat', choices=[0,1,2],type=int )
    parser.add_argument('-a','--alpha', help='alpha (transparency) ', action='store',default='0.3',  dest='alpha', type=float )
    parser.add_argument('-t','--thickness', help='thickness (of font) ', action='store',default='2',  dest='thickness', type=int )
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
    fdate=""
    if(opt.dateformat==0):
        fodate="%d %b, %Y"
    elif (opt.dateformat==1):
        fodate="%m-%d-%Y"
    elif (opt.dateformat==2):
        fodate="%m/%d/%Y"

    d=(today.strftime(fodate))
# Stamp the message on image lower right corner 
    cv2.putText(overlay, d, (int(width/10),int (2+height/8)), int(opt.font), 2.5, (255,255,255), thickness=opt.thickness)
    cv2.putText(overlay, opt.message, (int(width/10),int (height/8*7)), cv2.FONT_HERSHEY_PLAIN, 2.5, (255,255,255), thickness=opt.thickness)
    if(verbose):
        cv2.imshow("overlay",overlay)
    cv2.addWeighted(overlay, opt.alpha, output, 1 - opt.alpha, 0, output)
    if(verbose):
        cv2.imshow("output",output)
# Save the image    
    cv2.imwrite(opt.imagefilename+".out.jpg", output)
    if(verbose):
        cv2.waitKey(15000)
        
 
