# from PIL import Image

# # im = Image.open("BN (2).jpg")
# img = Image.open("BN (2).jpg")
# w, h = img.size
# cropped_img = img.crop(((w-2000)//2, (h-2000)//2, (w+2000)//2, (h+2000)//2))
# cropped_img.show()
################ New Prpgram start here ####################
from PIL import Image
im = Image.open('BN (3).jpg')

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

im_new = crop_max_square(im)
im_new.show()