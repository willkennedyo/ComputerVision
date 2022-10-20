import cv2
import os
from imutils import paths
import shutil

def listImages(path, folder):
    imagemPath = list(paths.list_images(path))
    filename = 1
    if not os.path.exists(folder):
        os.makedirs(folder)

    for image in imagemPath:
        image.replace(image, folder+"/"+str(filename)+".png")
        shutil.copy(image, image.replace(image, folder+"/"+str(filename)+".png"))

        grayscaleImage = cv2.imread(folder+"/" + str(filename) + ".png", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(grayscaleImage, (100, 100))
        cv2.imwrite(folder+"/" + str(filename) + ".png", resized_image)

        print(image.replace(image, folder+"/"+str(filename)+".png"))

        filename += 1

def create_pos_n_neg(negativeFolder, positiveFolder):
    for file_type in [negativeFolder]:
        for img in os.listdir(file_type):
            if file_type == positiveFolder:
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

catsPathReference = 'images/cats'
catsPath = 'cat'

dogsPathReference = 'images/dogs'
dogsPath = 'dog'

listImages(catsPathReference,catsPath)

listImages(dogsPathReference,dogsPath)

create_pos_n_neg(dogsPath,catsPath)