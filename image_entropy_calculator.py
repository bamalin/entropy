import os
import numpy as np
import cv2
from scipy.stats import entropy
import pandas as pd

root = "D:/PCB-P Dataset/"
_bins = 128
i=0

all_data = []
image_data = []
for roots, dirs, files in os.walk(root):
    for dir in dirs:
        for roots2, dirs2, files2 in os.walk(root+dir+'/'):
            for dir2 in dirs2:
                for roots3,dirs3,files3 in os.walk(root+dir+'/'+dir2+'/'):
                    for file3 in files3:
                        board = file3[0]
                        perspective = file3[1:3]
                        rotation = file3[3]
                        image = cv2.imread(root+dir+'/'+dir2+'/'+file3)
                        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                        hist, _ = np.histogram(gray_image.ravel(), bins=_bins, range=(0, _bins))
                        prob_dist = hist / hist.sum()
                        image_entropy = entropy(prob_dist, base=2)
                        a = []
                        a.append(board)
                        a.append(perspective)
                        a.append(rotation)
                        a.append(image_entropy)
                        b = (hist.tolist())
                        for col in b:
                            a.append(col)

                        all_data.append(a)
                        #image_data.append(board,image_entropy,hist])


df = pd.DataFrame(all_data)
df.to_excel("D:/PhD/Entropy/PCB-P/PCB-P Pers Rot Grayscale Histogram Flattened No Norm.xlsx")

                        #print(f"Image Entropy {image_entropy}")
