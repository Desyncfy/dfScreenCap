# Thank you mcpixelate, you're exactly what I need and you have 1 (now 2) stars and no updates for 5 years.
from mcpixelate.mcpixelate.mcpixelate import PixelImage
from PIL import ImageGrab
import os

# Logic™
def getScreenToCSV(saveImage=False):
    latest = ImageGrab.grab()
    os.remove("latest.png")
    latest.save("latest.png")
    image = PixelImage("latest.png", 50, 50, 50)
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
            outputnested = []
            for item in line.split(","):
                item = item.strip("\n,")
                countnested += 1
                if countnested == 1: # X
                    outputnested.append(f'"hypercube:x{count}": {item}.0d')
                    print(f'x: {item}')
                elif countnested == 2: # Y
                    print(f'y: {item}')
                    outputnested.append(f'"hypercube:y{count}": {item}.0d')
                elif countnested == 3: # Block
                    outputnested.append(f'"hypercube:block{count}": "{item}"')
                    print(f'block: {item}, line: {line}')
            output.append(",".join(outputnested))
        return ",".join(output)
