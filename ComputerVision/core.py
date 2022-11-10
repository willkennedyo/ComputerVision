import numpy as np
import cv2
from PIL import ImageGrab

class Object:
    def __init__(self, path):
        img = cv2.imread(path, 0)
        self.img = img
        if(img.shape != None):
            self.width = img.shape[1]
            self.height = img.shape[0]
        self.location = None

    def match(self, scr):
        correlatedTemplate = cv2.matchTemplate(scr, self.img, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(correlatedTemplate)
        startLoc = maxLoc
        endLoc = (startLoc[0]+self.width, startLoc[1]+self.height)

        if maxVal > 0.8: # similarity in 80% or greater
            self.location = (startLoc, endLoc)
            return True
        else:
            self.location = None
            return False

def grabScreen(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    img = np.array(img)
    # Pillow uses RGB and OpenCV uses BGR, so it is necessary to convert the colors pattern
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img