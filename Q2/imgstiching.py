import numpy as np
import cv2

imgPath=["Test1/A1.jpg","Test1/A2.jpg","Test1/A3.jpg"]

imgPath2=["Test2/bookstore1.jpg","Test2/bookstore2.jpg","Test2/bookstore3.jpg"]

imgPath3=["Test3/bookstore5.jpg","Test3/bookstore6.jpg","Test3/bookstore7.jpg"]

imgPath4=["Test4/sci1.jpg","Test4/sci2.jpg","Test4/sci3.jpg"]

imgPath5=["Test5/urban1.jpg","Test5/urban2.jpg","Test5/urban3.jpg"]

images = []

for path in imgPath5:
	image = cv2.imread(path)
	images.append(image)

print(len(images))
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("Image Stitching Successful")
	cv2.imshow("Stitched Image", stitched)
	cv2.imwrite("stitched5.png", stitched)
	cv2.waitKey(0)
else:
	print("[INFO] Failed Image Stitching ({})"/format(status))
