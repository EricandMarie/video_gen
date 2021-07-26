from PIL import Image
import PIL
import random

width = input("Largeur des images (défaut 1920) : ")
if width == "":
    width = 1920
else:
    width = int(width)

height = input("Hauteur des images (défaut 1080) : ")
if height == "":
    height = 1080
else:
    height = int(height)

nbImages = int(input("Nombre d'images : "))

print("\nEstimation du temps : " + str(nbImages // 780) + "min" + str(int((nbImages / 13) % 60)) + "s")

i = 1
while i < nbImages+1:
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    nb = random.randrange(1, 2)
    j = 0
    im = PIL.Image.new(mode="RGB", size=(width, height), color=(r, g, b))
    while i < nbImages+1 and j < nb:
        im1 = im.save("images/"+"0"*(4-len(str(i)))+str(i)+".jpg")
        i += 1
        j += 1

print("Création des images terminée")