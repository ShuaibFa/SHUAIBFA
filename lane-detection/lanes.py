import cv2
import numpy as np
def canny(image) :
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY) #GRAYSCALE
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image) :
    height = image.shape[0]
    polygons = np.array( [
    [(255, height ) , (805, height ),(555 , 270)] ] )
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask

image = cv2.imread('straight_lines.jpeg')
lane_image = np.copy(image)
canny = canny(lane_image)
cv2.imshow("result", region_of_interest(canny))
cv2.waitKey(0)
