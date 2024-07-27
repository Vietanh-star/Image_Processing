import cv2 as cv
import numpy as np
# KNN - K Nearest Neighbors la thuat toan so sanh ma tran cua OpenCV, khi dua vao 1 ma tran test, no se
# tim cac phan tu trong ma tran Traning gan voi ma tran test nhat roi assign Labels tuong ung
# voi ma tran test do.

# if read color imread('path', defaut = 1) -> each pixel = [r,g,b]
# if read simple imread('path', 0) -> each pixel = [0-255] 
img = cv.imread('digits.png', 0)

# split 1 picture (2000x1000 pixel) to Numbers[50 row, 100 column], each item has 20x20 pixel
cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]

# convert <list> to <numpy.ndarray>
x = np.array(cells)

# convert [[..] [..] [..]] (array 2 dict)  to  [.. .. ..] (array 1 dict)
training = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
test2 = x[12, 99].reshape(-1, 400).astype(np.float32)

# create <numpy.ndarray> [0 1 2 .. 8 9]
k = np.arange(10)  

# np.repeat(k, 250)  ->  [0 0 0....1 1 1...2 2 2....9 9 9 9]    we have 250 number 0, 250 number 1, .. 250 number 9
# [:, np.newasix]    ->  convert to [[0] [0] [0] ... [1] [1] [1] ... [2] [2] [2] ... [9] [9] [9]]
trainLabels = np.repeat(k, 250)[:, np.newaxis]

knn = cv.ml.KNearest.create()
knn.train(training, 0, trainLabels)
retval, results, neighbors, dist = knn.findNearest(test2, 5)

print('retval'      , retval)       # return value type float - summary 1 result in total list result below
print('results'     , results)      # return list result('trainLabels' assign on)
print('neighbors'   , neighbors)    # return 5 item(labels assign) nearest test param
print('dist'        , dist)         # return 5 distance from param test to 5 neighbors nearest

