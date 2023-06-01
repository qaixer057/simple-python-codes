from PIL import Image
im = Image.open("BN (2).jpg")
width, height = im.size   # Get dimensions

# new_width = width/2 
# new_height = height/2

new_width = 1500
new_height = 1500

left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

# Crop the center of the image
im = im.crop((left, top, right, bottom))

im.show()
