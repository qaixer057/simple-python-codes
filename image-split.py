#Python Code to split the images in equal grids of provided size
#Uses python image_slicer module for spliting the images
# pip install image_slicer
import image_slicer
import os
import sys

path = "H:\\Sliced\\Benign\\"

dirs = os.listdir( path )

def split():
    for item in dirs:
        if os.path.isfile(path+item):
        	image_slicer.slice(path+item, 12) # instead of 12, specify this number for grids i.e. number of slices
        	print("Done with Slicing...!!!")
split()
