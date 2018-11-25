import cv2


def drawlines(imgL, imgR, lines, pts1, pts2):
    ''' imgL - image on which we draw the epilines for the points in imgR
        lines - corresponding epilines '''
    r, c = imgL.shape
    imgL = cv2.cvtColor(imgL, cv2.COLOR_GRAY2BGR)
    imgR = cv2.cvtColor(imgR, cv2.COLOR_GRAY2BGR)
    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        x0, y0 = map(int, [0, -r[2] / r[1]])
        x1, y1 = map(int, [c, -(r[2] + r[0] * c) / r[1]])
        cv2.line(imgL, (x0, y0), (x1, y1), color, 1)
        cv2.circle(imgL, tuple(pt1), 5, color, -1)
        cv2.circle(imgR, tuple(pt2), 5, color, -1)
    return imgL, imgR
