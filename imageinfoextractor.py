import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import os
import hashlib
import PIL

__author__ = 'Daniel Zidelis'

#search through the directory and loops through all of the files
def Main():
        for f in os.listdir('.'):
                #checks if the file has an image extension
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                        metaData = {}
                        i = Image.open(f)
                        #splits the file name into name, and extension and saves to fn
                        fn, fext = os.path.splitext(f)
                        #creates name of the outfile for the specific image
                        outfile = fn +".txt"
                        #deletes text file for specific file so that it does not just append
                        #to the end of the text file
                        if os.path.exists(outfile):
                                os.remove(outfile)
                        print("Getting meta data... of ", f)
                        info = i._getexif()
                        if info:
                                print("found meta data")
                                for (tag, value) in info.items():
                                        tagname = TAGS.get(tag, tag)
                                        metaData[tagname] = value
                                        #loops through and appends the tags to the text file
                                with open(outfile, 'a+') as f:
                                        for(tagname, value) in metaData.items():
                                                f.write(str(tagname)+"\t"+\
                                                str(value)+"\n")


if __name__ == '__main__':
    Main()
