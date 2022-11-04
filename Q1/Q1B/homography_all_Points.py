import cv2
import numpy as np
import matplotlib.pyplot as plt

src_points = np.array([[374,479],[328,634],[1100,636],[1069,567],[780,565]])
dest_points = np.array([[518,593],[526,440],[630,305],[698,342],[726,244]])


h, status = cv2.findHomography(src_points, dest_points)
print(h)
im_src = cv2.imread('img1grayscale.png')
im_dst = cv2.imread('img2grayscale.png')


im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()
# IMG 1 COORDINATES
# 374   479
# 328   634
# 1100   636
# 1069   567
# 780   565

# 518   593
# 526   440
# 630   305
# 698   342
# 726   244



