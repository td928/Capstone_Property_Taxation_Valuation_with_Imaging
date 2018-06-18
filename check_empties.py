import pandas
from PIL import Image
import cv2
import glob
import numpy as np
import os 

images = glob.glob('google_street_image/*/*.jpg')[229000:]

j = 0
for i in images:
    #if set(np.asarray(Image.open(i)).reshape(640*640*3,).tolist()) == 1:
    try: 
        if sum(np.asarray(Image.open(i))[0,0,:]) == 678:
            print(i)
    except:
        os.remove(i)
        print("{} deleted cuz it's not permitted to read".format(i))
    if j % 1000 == 0:
        print("{}/{} finished".format(j,len(images)))
    j += 1