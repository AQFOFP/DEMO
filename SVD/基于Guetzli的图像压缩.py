import pyguetzli
from PIL import Image

from time import strftime, localtime

# 打印当前时间
def printTime():
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    return

printTime()
image = Image.open("sender.png")
optimized_jpeg = pyguetzli.process_pil_image(image, 60)

output = open("sender_new.png", "wb")
output.write(optimized_jpeg)
printTime()