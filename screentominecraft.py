# Thank you mcpixelate, you're exactly what I need and you have 1 (now 2) stars and no updates for 5 years.
from mcpixelate.mcpixelate.mcpixelate import PixelImage
from PIL import ImageGrab

# Logic™
def getScreenToCSV(saveImage=False):
    latest = ImageGrab.grab()
    latest.save("latest.png")
    image = PixelImage("latest.png", 50, 50, 50)
    if saveImage == True:
        image.save_image("frame.png")
    image.csv_coords("latest.csv")
