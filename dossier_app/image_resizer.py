import PIL
from PIL import Image

# add path for image open, and create path/name for image save
# then run.

basewidth = 600
img = Image.open()
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save()
