# Thank you mcpixelate, you're exactly what I need and you have 1 (now 2) stars and no updates for 5 years.
from mcpixelate.mcpixelate.mcpixelate import PixelImage
from PIL import ImageGrab
import os

# Logic™
def getScreenToCSV(saveImage=False):
    latest = ImageGrab.grab()
    os.remove("latest.png")
    latest.save("latest.png")
    image = PixelImage("latest.png", 84, 100, 100)
    if saveImage == True:
        image.save_image("frame.png")
    os.remove("latest.csv")
    image.csv_coords("latest.csv")


def readCSV(filename):
    count = 0
    with open(filename) as csv:
        output = []
        for line in csv:
            count += 1
            if count == 1:
                continue
            countnested = 0
            outputnested = ""
            for item in line.split(","):
                item = item.strip("\n,")
                countnested += 1
                if countnested == 1: # X
                    outputnested += f'"hypercube:data{count-1}": "{item},'
                elif countnested == 2: # Y
                    outputnested += f'{item},'
                elif countnested == 3: # Block
                    outputnested += f'{item}"'
            output.append(outputnested)
        return ",".join(output)
