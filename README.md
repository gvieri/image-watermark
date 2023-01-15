# image-watermark
A simple python utility to watermark images with date [upper left] and a (short) message bottome left. 

Usage python image_watermark.py -i <image file name> [-m message to be watermarked] [-f font, possible values 0 to 7 default is 0] [-a alpha trasparency] [-v verbose it show the preview of the result image and the message to be embedded]

please enjoy. 

## option list (from help)
```
$ python image-watermark.py 
usage: image-watermark.py [-h] -i IMAGEFILENAME [-m MESSAGE]
                          [-f {0,1,2,3,4,5,6,7}] [-d {0,1,2}] [-a ALPHA]
                          [-t THICKNESS] [-v]

$ python image-watermark.py -h
usage: image-watermark.py [-h] -i IMAGEFILENAME [-m MESSAGE]
                          [-f {0,1,2,3,4,5,6,7}] [-d {0,1,2}] [-a ALPHA]
                          [-t THICKNESS] [-v]

This simple program will help you to watermark an image. The -i parameter is
the image file name. This name will be added of a ".out." between the file
name and the extension. The resulting name will be used for the output file.

options:
  -h, --help            show this help message and exit
  -i IMAGEFILENAME, --imagename IMAGEFILENAME
                        image file name
  -m MESSAGE, --message MESSAGE
                        message to be watermark (you can use "" to insert more
                        words
  -f {0,1,2,3,4,5,6,7}, --font {0,1,2,3,4,5,6,7}
                        font
  -d {0,1,2}, --dateformat {0,1,2}
                        dateformat 0 for 12 Jun, 2018, 1 for 2018-06-12, 2 for
                        06/12/2018
  -a ALPHA, --alpha ALPHA
                        alpha (transparency)
  -t THICKNESS, --thickness THICKNESS
                        thickness (of font)
  -v, --verbose         more verbose output
```

##Example of use:

