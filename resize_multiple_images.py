from PIL import Image
import os, sys
#X:\Acral  Melanoma\224 by 224\Dermoscopic images of benign nevi
# path = "X:\\Thesis\\data\\validation\\acral\\"
#C:\Users\user\Desktop\data\data\validation\am
path = "C:\\Users\\user\\Desktop\\data\\data\\validation\\am\\"
# path = "/root/Desktop/python/images/"
dirs = os.listdir( path )
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((32,32), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
