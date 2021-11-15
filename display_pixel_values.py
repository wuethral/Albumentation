from PIL import Image
import cv2 as cv
import os
import numpy as np
import torch
import pandas as pd

img = Image.open('1.png')
#print(np.array(img)[4:7, 4:7])
im_t = torch.tensor(img)
df = pd.DataFrame(im_t[4:15, 4:22])
print(df)