from PIL import Image

src = "ImageLayerX.jpeg"
img = Image.open(src).convert('L')

# these series replaces light pollution with black pixels
# the if statement integers can be altered to match the image being used
# add extra conditions to the if statement if needed


for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixel = img.getpixel((x,y))
        if(pixel/5 < 15):
            img.putpixel((x,y), 0)

# I used this when I couldn't filter light pollution in the middle of image
# without reducing the number of stars visible
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixel = img.getpixel((x,y))
        if(pixel/5 < 18 or y>1100 or (y>600 and x<2400)):
            img.putpixel((x,y), 0)

img.save('StarLayerX.jpg')
