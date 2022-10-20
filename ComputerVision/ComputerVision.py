import cv2
import os
from imutils import paths
import shutil

def listImages(path, folder):
    imagemPath = list(paths.list_images(path))
    numero = 1
    if not os.path.exists(folder):
        os.makedirs(folder)

    for image in imagemPath:
        image.replace(image, folder+"/"+str(numero)+".png")
        shutil.copy(image, image.replace(image, folder+"/"+str(numero)+".png"))

        grayscaleImage = cv2.imread(folder+"/" + str(numero) + ".png", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(grayscaleImage, (100, 100))
        cv2.imwrite(folder+"/" + str(numero) + ".png", resized_image)

        print(image.replace(image, folder+"/"+str(numero)+".png"))

        numero += 1

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

listImages('images/cats','cat')
listImages('images/dogs','dog')
create_pos_n_neg('dog','cat')

#import cv2

#algorithm = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

#colouredImage = cv2.imread('photos/2.jpg')


#grayscaleImage = cv2.cvtColor(colouredImage, cv2.COLOR_BGR2GRAY)

#faces = algorithm.detectMultiScale(grayscaleImage)

#print(faces)

#for(x, y, l, a) in faces:
#    cv2.rectangle(colouredImage, (x, y), (x + l, y + a), (0, 255, 0), 2)

#cv2.imshow("Faces", colouredImage)
#cv2.waitKey()