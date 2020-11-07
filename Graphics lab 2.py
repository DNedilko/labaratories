
import PIL
from PIL import Image, ImageDraw
f1=open('DS1.txt', 'r')
data=f1.readlines()
xy=[]
for i in data:
    x,y=i.split(" ")
    xy.append(int(y))
    xy.append(int(x))

print(xy)

im = PIL.Image.new(mode = "RGB", size = (960,540), color = (255, 255, 255) )
draw=PIL.ImageDraw.Draw(im)
draw.point(xy, fill=(0,0,0))
im.show()
im.save("DS1 painted.png","PNG")