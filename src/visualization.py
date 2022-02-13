import cv2
import numpy as np
from moviepy.editor import *


def get_index(arr, x):
    loc = [0, 0]
    location = np.where(arr == x)
    loc[1] = int(location[1])
    loc[0] = int(location[0])
    return loc


def create_state(img, loc, puzzle, h, w):
    puzzle[(loc[0] * w):((loc[0] + 1) * h), (loc[1] * w):((loc[1] + 1) * h), :] = img
    return puzzle


def visualize(lines):
    path_array = np.zeros((len(lines), 4, 4), int)
    for i in range(0, len(lines)):
        path_array[i, :, :] = (np.reshape(np.asarray(lines[i].split()), (4, 4))).T

    im0 = cv2.imread("../media/visualization/0.png")
    im0 = cv2.resize(im0, (270, 270), interpolation=cv2.INTER_AREA)
    im1 = cv2.imread("../media/visualization/1.png")
    im1 = cv2.resize(im1, (270, 270), interpolation=cv2.INTER_AREA)
    im2 = cv2.imread("../media/visualization/2.png")
    im2 = cv2.resize(im2, (270, 270), interpolation=cv2.INTER_AREA)
    im3 = cv2.imread("../media/visualization/3.png")
    im3 = cv2.resize(im3, (270, 270), interpolation=cv2.INTER_AREA)
    im4 = cv2.imread("../media/visualization/4.png")
    im4 = cv2.resize(im4, (270, 270), interpolation=cv2.INTER_AREA)
    im5 = cv2.imread("../media/visualization/5.png")
    im5 = cv2.resize(im5, (270, 270), interpolation=cv2.INTER_AREA)
    im6 = cv2.imread("../media/visualization/6.png")
    im6 = cv2.resize(im6, (270, 270), interpolation=cv2.INTER_AREA)
    im7 = cv2.imread("../media/visualization/7.png")
    im7 = cv2.resize(im7, (270, 270), interpolation=cv2.INTER_AREA)
    im8 = cv2.imread("../media/visualization/8.png")
    im8 = cv2.resize(im8, (270, 270), interpolation=cv2.INTER_AREA)
    im9 = cv2.imread("../media/visualization/9.png")
    im9 = cv2.resize(im9, (270, 270), interpolation=cv2.INTER_AREA)
    im10 = cv2.imread("../media/visualization/10.png")
    im10 = cv2.resize(im10, (270, 270), interpolation=cv2.INTER_AREA)
    im11 = cv2.imread("../media/visualization/11.png")
    im11 = cv2.resize(im11, (270, 270), interpolation=cv2.INTER_AREA)
    im12 = cv2.imread("../media/visualization/12.png")
    im12 = cv2.resize(im12, (270, 270), interpolation=cv2.INTER_AREA)
    im13 = cv2.imread("../media/visualization/13.png")
    im13 = cv2.resize(im13, (270, 270), interpolation=cv2.INTER_AREA)
    im14 = cv2.imread("../media/visualization/14.png")
    im14 = cv2.resize(im14, (270, 270), interpolation=cv2.INTER_AREA)
    im15 = cv2.imread("../media/visualization/15.png")
    im15 = cv2.resize(im15, (270, 270), interpolation=cv2.INTER_AREA)

    h, w, _ = im0.shape

    fps = len(lines) / 3.5
    puzzle = np.zeros([h * 4, w * 4, 3])
    path = "../output/Visualization.mp4"
    vis = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w * 4, h * 4))
    for i in range(0, len(lines)):
        loc_0 = get_index(path_array[i], 0)
        loc_1 = get_index(path_array[i], 1)
        loc_2 = get_index(path_array[i], 2)
        loc_3 = get_index(path_array[i], 3)
        loc_4 = get_index(path_array[i], 4)
        loc_5 = get_index(path_array[i], 5)
        loc_6 = get_index(path_array[i], 6)
        loc_7 = get_index(path_array[i], 7)
        loc_8 = get_index(path_array[i], 8)
        loc_9 = get_index(path_array[i], 9)
        loc_10 = get_index(path_array[i], 10)
        loc_11 = get_index(path_array[i], 11)
        loc_12 = get_index(path_array[i], 12)
        loc_13 = get_index(path_array[i], 13)
        loc_14 = get_index(path_array[i], 14)
        loc_15 = get_index(path_array[i], 15)
        create_state(im0, loc_0, puzzle, h, w)
        create_state(im1, loc_1, puzzle, h, w)
        create_state(im2, loc_2, puzzle, h, w)
        create_state(im3, loc_3, puzzle, h, w)
        create_state(im4, loc_4, puzzle, h, w)
        create_state(im5, loc_5, puzzle, h, w)
        create_state(im6, loc_6, puzzle, h, w)
        create_state(im7, loc_7, puzzle, h, w)
        create_state(im8, loc_8, puzzle, h, w)
        create_state(im9, loc_9, puzzle, h, w)
        create_state(im10, loc_10, puzzle, h, w)
        create_state(im11, loc_11, puzzle, h, w)
        create_state(im12, loc_12, puzzle, h, w)
        create_state(im13, loc_13, puzzle, h, w)
        create_state(im14, loc_14, puzzle, h, w)
        create_state(im15, loc_15, puzzle, h, w)
        puzzle = puzzle.astype(np.uint8)
        vis.write(puzzle)
        cv2.imshow("Puzzle", puzzle)
        cv2.waitKey(250)

    vis.write(puzzle)
    vis and vis.release()
    cv2.destroyAllWindows()
    clip = VideoFileClip(path)
    clip.write_gif("../media/gif/Vis.gif")

with open("../output/nodePath_testcase.txt") as f:
    lines = f.readlines()

visualize(lines)