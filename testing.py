import cv2
import numpy as np
import os

SPLIT_LOCATION = 11720
RESIZE_SIZE = (1280, 720)

CHOICE = 0
PATH = "C:/Users/caperren/Pictures/FAILED IMAGES/scanner 1"
PATHS = [os.path.join(PATH, item) for item in os.listdir(PATH)]

MEDIAN_BLUR_AMOUNT = 5  # Adjustable???

MIN_RADIUS = 365
MAX_RADIUS = 415

MIN_DIST_BETWEEN = 800

CENTER_VALUE = 50
SIGMA = 0.75

if __name__ == '__main__':
    while True:
        full_plate_image = cv2.imread(PATHS[CHOICE])
        full_plate_image = cv2.rotate(full_plate_image, 0)
        full_plate_image = cv2.flip(full_plate_image, 0)

        height, width, type = full_plate_image.shape
        print(full_plate_image.shape)

        top_image = full_plate_image[0:height, 0:SPLIT_LOCATION].copy()
        top_image = cv2.medianBlur(top_image, MEDIAN_BLUR_AMOUNT)
        top_image_gray = cv2.cvtColor(top_image, cv2.COLOR_BGR2GRAY)

        bottom_image = full_plate_image[0:height, SPLIT_LOCATION:width].copy()
        bottom_image = cv2.medianBlur(bottom_image, MEDIAN_BLUR_AMOUNT)
        bottom_image_gray = cv2.cvtColor(bottom_image, cv2.COLOR_BGR2GRAY)

        top_median = np.median(top_image_gray)
        top_lower = int(max(1, (1.0 - SIGMA) * CENTER_VALUE))
        top_upper = int(min(255, (1.0 + SIGMA) * CENTER_VALUE))
        print(top_median, top_lower, top_upper)

        circles_top = cv2.HoughCircles(top_image_gray, cv2.HOUGH_GRADIENT, 1, MIN_DIST_BETWEEN, param1=top_lower,
                                       param2=top_upper, minRadius=MIN_RADIUS, maxRadius=MAX_RADIUS)
        circles_top = np.uint16(np.around(circles_top))

        circles_bottom = cv2.HoughCircles(bottom_image_gray, cv2.HOUGH_GRADIENT, 1, MIN_DIST_BETWEEN, param1=top_lower,
                                          param2=top_upper, minRadius=MIN_RADIUS, maxRadius=MAX_RADIUS)
        circles_bottom = np.uint16(np.around(circles_bottom))
        print(len(circles_top[0, :]), len(circles_bottom[0, :]))

        for i in circles_top[0, :]:
            # draw the outer circle
            cv2.circle(top_image, (i[0], i[1]), i[2], (0, 255, 0), 20)
            # draw the center of the circle
            cv2.circle(top_image, (i[0], i[1]), 40, (0, 0, 255), -1)

        for i in circles_bottom[0, :]:
            # draw the outer circle
            cv2.circle(bottom_image, (i[0], i[1]), i[2], (0, 255, 0), 20)
            # draw the center of the circle
            cv2.circle(bottom_image, (i[0], i[1]), 40, (0, 0, 255), -1)

        top_resized = cv2.resize(top_image, RESIZE_SIZE)
        bottom_resized = cv2.resize(bottom_image, RESIZE_SIZE)

        cv2.imshow("top", top_resized)
        cv2.imshow("bottom", bottom_resized)

        if cv2.waitKey() & 0xFF == ord('q'):
            exit()
        else:
            CHOICE += 1
            cv2.destroyAllWindows()
