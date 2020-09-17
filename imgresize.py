import cv2
import os 
import sys

scale = 4
path = "/home/lily/delta/0713_data/stacked_data_0807/zedmini"
path_save = "/home/lily/delta/0713_data/stacked_data_0807/zedmini_2/"
# filename = "unity.png"
#1280*720

x = 120
y = 240
w = 640
h = 480

img_2 = None

os.makedirs(path_save, exist_ok=True)
for root, dirs, files in os.walk(path): 
    for f in files:
        if os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg':
        	img = cv2.imread(os.path.join(path, f))
        	# img_2 = cv2.resize(img, (int(img.shape[1]/scale), int(img.shape[0]/scale)), interpolation=cv2.INTER_CUBIC)
        	img_2 = img[y:y+h, x:x+w]
        	cv2.imwrite(path_save+str(f), img_2)

# img = cv2.imread(path + filename)
# img_2 = cv2.resize(img, (int(img.shape[1]/scale), int(img.shape[0]/scale)), interpolation=cv2.INTER_CUBIC)
# cv2.imwrite(path + "2/" + filename, img_2)
# img = cv2.imread("/home/lily/delta/0713_data/zedmini/color_0000.jpg")
# img_2 = img[y:y+h, x:x+w]
# cv2.imshow("resize", img_2)
# cv2.waitKey(0)