from ppadb.client import Client
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw

class Device:
    device = None
    screenshotOutput = ""

    def __init__(self):
        self.device = self.getDevice()
        self.screenshotOutput = "screen.png"

    def getDevice(self):
        adb = Client(host='127.0.0.1', port=5037)
        devices = adb.devices()
        if len(devices) == 0:
            print("No devices found!")
            exit()
        return devices[0]

    def getAllButtons(self, img_name):
        locations = []
        self.refreshScreenshot()
        while True:
            data = self.getButton(img_name)
            if not data: break
            pos1, pos2 = data
            
            locations.append((pos1, pos2))
            maskArea(self.screenshotOutput, pos1,pos2)
        return locations

    def getButton(self, img_name):
        img = cv.imread(self.screenshotOutput,0).copy()
        template = cv.imread(f'./assets/{img_name}.png',0)
        w, h = template.shape[::-1]
        method = eval('cv.TM_CCOEFF_NORMED')
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if max_val < 0.9: return ()
        # pixels = np.array(Image.open(self.screenshotOutput), dtype=np.uint8)#[min_loc[0]:min_loc[1]] #[max_loc[0]:max_loc[1]]
        return max_loc, (max_loc[0] + w, max_loc[1] + h)

    def refreshScreenshot(self):
        image = self.device.screencap()
        with open(self.screenshotOutput, 'wb') as f: f.write(image)

    
def maskArea(image, pos1, pos2):
    with Image.open(image) as im:
        im = Image.open(image)
        draw = ImageDraw.Draw(im)
        area = (pos1[0], pos1[1], pos2[0], pos2[1])
        draw.rectangle(area, fill = 0)
        im.save(image)