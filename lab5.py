import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh grayscale
img = cv.imread('messi5.jpg', 0)

# Kiểm tra ảnh
if img is None:
    print("Không đọc được ảnh")
    exit()

# Tạo mảng histogram 256 mức xám
hist = [0] * 256

# Duyệt từng pixel và đếm
for row in img:
    for pixel in row:
        hist[pixel] += 1

# Hiển thị ảnh
cv.imshow('Original Image', img)

# Vẽ histogram
plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Gray Level')
plt.ylabel('Number of Pixels')

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()