import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image


def cropImage(imageName, realName):
    myimg = Image.open(imageName)
    width = myimg.size[0]
    height = myimg.size[1]
    BORDER_SIZE_LEFT = int(width*0.055)
    BORDER_SIZE_TOP = int(height*0.02)

    a_img = myimg.crop((BORDER_SIZE_LEFT, BORDER_SIZE_TOP, width//2, height-BORDER_SIZE_TOP))
    b_img = myimg.crop((width//2, BORDER_SIZE_TOP, width-BORDER_SIZE_LEFT, height-BORDER_SIZE_TOP))

    a_img.convert('RGB').save('cropedImages/'+realName+'_a.jpeg')
    b_img.convert('RGB').save('cropedImages/'+realName+'_b.jpeg')


def loadImages():
    url = urlopen('https://picasaweb.google.com/109578654150408610323/DixitAll')
    soup = BeautifulSoup(url)
    if not os.path.exists('img'):
        os.makedirs('img')
    if not os.path.exists('cropedImages'):
        os.makedirs('cropedImages')
    i = 0
    for img in soup.find_all('img'):
        i+=1
        print(img)
        img_url = img['src'].replace('s128', 's1243')
        image = urlopen(img_url).read()
        imgName = 'img/'+str(i)+'.jpeg'
        f = open(imgName, 'wb')
        f.write(image)
        f.close()
        try:
            cropImage(imgName, str(i))
        except SystemError:
            continue

loadImages()