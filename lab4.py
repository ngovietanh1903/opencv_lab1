import cv2 as cv
import numpy as np

# Đọc ảnh grayscale
img = cv.imread('messi5.jpg', 0)

# Kiểm tra ảnh
if img is None:
    print("Không đọc được ảnh")
    exit()

# 1. Âm bản
negative = 255 - img

# 2. Tăng sáng
bright = cv.add(img, 50)

# 3. Giảm sáng
dark = cv.subtract(img, 50)

# 4. Threshold nhị phân
_, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Hiển thị kết quả
cv.imshow('Original', img)
cv.imshow('Negative', negative)
cv.imshow('Bright', bright)
cv.imshow('Dark', dark)
cv.imshow('Threshold', thresh)

cv.waitKey(0)
cv.destroyAllWindows()