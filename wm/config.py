from PIL import Image, ImageDraw, ImageFont

width = 240
height = 15

image = Image.new('RGB', (width, height))
font = ImageFont.truetype('wqy-zenhei.ttc',12)

draw = ImageDraw.Draw(image)
draw.text((3,1),'测试',font=font,fill=0xFFFFFF)

#  image.save('./test.jpg','jpeg')
image.show()

