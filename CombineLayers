from PIL import Image

#you can use as many layers as you'd like, but obviously it will be slower the more you use
imgL1 = Image.open("Stars8-14-layer1.jpg")
imgL2 = Image.open("Stars8-14-layer2.jpg")
imgL3 = Image.open("Stars8-14-layer3.jpg")

for x in range(img.size[0]):
    for y in range(img.size[1]):

        # copy and paste for each layer you use
        pixel1 = imgL1.getpixel((x,y))
        pixel2 = imgL2.getpixel((x,y))
        pixel3 = imgL3.getpixel((x,y))

        # get the max of all the layers.  This will include all the stars found in all images
        pixel = max(pixel1, pixel2, pixel3)
        img.putpixel((x, y), pixel)

#img.show()
img.save('Stars-final.jpg')
