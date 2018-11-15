import cv2
import numpy as np

RED = (255, 0, 0)
GREEN = (0, 255, 0)

WELL_WALL_LINE_THICKNESS = 20

WELL_CENTER_RADIUS = 40
WELL_CENTER_LINE_THICKNESS = -1  # -1 is filled in circle


def find_wells_in_image(image_rgb, config):
    blurred = cv2.medianBlur(image_rgb, config["blur"])
    image_gray = cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY)

    wells = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, 1, config["min_distance_between"],
                             param1=config["threshold_1"], param2=config["threshold_2"],
                             minRadius=config["min_radius"], maxRadius=config["max_radius"])

    if wells is not None:
        wells = np.uint16(np.around(wells))[0, :]

        # Sort wells into form A1, A2, ..., B1, B2, ...


    return wells


def draw_wells_on_image(image, wells):
    if wells is not None:
        for i in wells:
            # draw the outer well
            cv2.circle(image, (i[0], i[1]), i[2], GREEN, WELL_WALL_LINE_THICKNESS)

            # draw the center of the well
            cv2.circle(image, (i[0], i[1]), WELL_CENTER_RADIUS, RED, WELL_CENTER_LINE_THICKNESS)
