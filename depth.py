# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# 
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# 
# 
# def calibrateCamera(img):
#     objPoints = []
#     imgPoints = []
# 
#     objp = np.zeros((6 * 7, 3), np.float32)
#     objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
# 
#     # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
#     hasCorners, corners = cv2.findChessboardCorners(img, (7, 6), None)
# 
#     if hasCorners:
#         objPoints.append(objp)
#         cv2.cornerSubPix(img, corners, (11, 11), (-1, -1), criteria)
#         imgPoints.append(corners)
#         # Draw and display the corners
#         cv2.drawChessboardCorners(img, (7, 6), corners, hasCorners)
#         cv2.imshow('img', img)
#         cv2.waitKey(500)
# 
#     ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, img.shape[::-1], None, None)
# 
#     return ret, mtx, dist, rvecs, tvecs
# 
# 
