import cv2
import cv2 as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

citra = cv2.imread('gunung.jpg',0)
ekual = cv2.equalizeHist(citra)
hasil = np.hstack((citra, ekual))
histo = cv.calcHist([ekual], [0], None, [256], [0, 256])

cv2.imshow("Hasil Equalisation",hasil)
plt.plot(histo)
plt.show()
cv2.waitKey(0)