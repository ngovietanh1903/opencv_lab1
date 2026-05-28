import cv2 as cv
import numpy as np

# Đọc ảnh
img = cv.imread("messi5.jpg")

if img is None:
    print("Không đọc được ảnh")
    exit()

# Chuyển sang ảnh xám
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Threshold để tạo ảnh nhị phân
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# Tìm contour
contours, hierarchy = cv.findContours(
    thresh,
    cv.RETR_TREE,
    cv.CHAIN_APPROX_SIMPLE
)

# Vẽ tất cả contour
draw = img.copy()

cv.drawContours(draw, contours, -1, (0,255,0), 2)

# In số lượng contour
print("So contour tim duoc:", len(contours))

# Lấy contour đầu tiên
cnt = contours[0]

# Tính diện tích
area = cv.contourArea(cnt)
print("Dien tich =", area)

# Tính chu vi
perimeter = cv.arcLength(cnt, True)
print("Chu vi =", perimeter)

# Bounding Rectangle
x, y, w, h = cv.boundingRect(cnt)

cv.rectangle(draw, (x,y), (x+w, y+h), (255,0,0), 2)

# Hiển thị
cv.imshow("Original", img)
cv.imshow("Threshold", thresh)
cv.imshow("Contours", draw)

cv.waitKey(0)
cv.destroyAllWindows()