import cv2 as cv
from PIL import Image
import numpy as np
import time

hold_button_time = 1
hold_button_basis = 1

def colorInPixelArray(color: np.array, pixels: np.array) -> bool:
    if type(color) == list:
        color = np.array(color)
    return (color == pixels).all(1).any()
    
def refreshScreenshot(device):
    image = getScreenShot(device)
    return image