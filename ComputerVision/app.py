import cv2
import numpy as np
import pyautogui as pag
import time

from PIL import ImageGrab
from core import Object, grabScreen
from const import Constants


def resize(img, scale = 1):
    scale_percent = scale # percent of original size
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)
  
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

# Set 1 to 100%, 2 to 200% or 3 to 300%
scale = 2

startTime = time.time()
prevTime = time.time()
speedRate = 1.5

player_index = 0
enemy_index = 0
distanceThreshold = 85

player = [ Object(Constants.WHITE_DINO), Object(Constants.BLACK_DINO)]
enemies = [
     [Object(Constants.WHITE_CACTUS_1),Object(Constants.WHITE_CACTUS_2),Object(Constants.WHITE_BIRD)], 
     [Object(Constants.BLACK_CACTUS_1), Object(Constants.BLACK_CACTUS_2), Object(Constants.BLACK_BIRD)]
]

while 1:
    img = grabScreen()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if player[0].match(img):
        topleft_x = int(player[0].location[0][0]- player[0].width)
        topleft_y = int(player[0].location[0][1] - 3*player[0].height)
        bottomRight_x = int(player[0].location[1][0]+14*player[0].width)
        bottomRight_y = int(player[0].location[1][1] + 0.5*player[0].height)
        screenStart = (topleft_x, topleft_y)
        screenEnd = (bottomRight_x, bottomRight_y)
        break

pag.press('space')

while 1:
    img_o = grabScreen(bbox=(*screenStart, *screenEnd))
    img = cv2.cvtColor(img_o, cv2.COLOR_BGR2GRAY)

    if player[0].match(img):
        player_index = 0
        enemy_index = 0
    elif player[1].match(img):
        player_index = 1
        enemy_index = 1
    
    if time.time() - prevTime > 1:
        if time.time() - startTime < 180 and player[player_index].location:
            distanceThreshold += speedRate
        
        prevTime = time.time()
    
    if player[player_index].location:
        cv2.rectangle(img_o, player[player_index].location[0], player[player_index].location[1], (255,0,0), 2)
    
    for enemy in enemies[enemy_index]:
        if enemy.match(img):
            cv2.rectangle(img_o, enemy.location[0], enemy.location[1], (0,0,255), 2)

            if player[player_index].location:
                horizontalDistance = enemy.location[0][0]-player[player_index].location[1][0]
                verticalDistance = player[player_index].location[0][1] - enemy.location[1][1]

                if horizontalDistance < distanceThreshold and verticalDistance < 2:
                    pag.press('space')
                    break


    cv2.imshow("Screen", resize(img_o,scale))

    if cv2.waitKey(1) == ord('q'):
        break