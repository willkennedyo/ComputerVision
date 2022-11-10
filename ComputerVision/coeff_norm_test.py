import cv2
from core import Object
from const import Constants

player = Object(Constants.WHITE_DINO)
screen = cv2.imread(Constants.SCREEN, 0)
    
correlatedTemplate= cv2.matchTemplate(screen, player.img, cv2.TM_CCOEFF_NORMED)
cv2.imshow('correlatedTemplate', correlatedTemplate)
cv2.waitKey(0)