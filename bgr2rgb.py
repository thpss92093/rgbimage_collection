#!/usr/bin/env python
import numpy as np
import cv2

image_rgb = cv2.imread("/home/lily/delta/0713_data/stacked_data_0807/d435_1/color_0011.jpg")
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)
cv2.imwrite("/home/lily/delta/0713_data/stacked_data_0807/d435_1/color_0011.jpg", image_rgb)




