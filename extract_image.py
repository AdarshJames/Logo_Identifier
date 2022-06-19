import numpy as np
import cv2

def extract_save(img,cordinates):
	img = img
	# # print(cordinates)
	# p1 = (89,425)
	# p2 = (106,303)
	# p3 = (217,318)
	# p4 = (200,440)
	pts = cordinates
	# print(pts)
	mask = np.zeros((img.shape[0], img.shape[1]))

	cv2.fillConvexPoly(mask, pts, 1)
	mask = mask.astype(np.bool)

	out = np.zeros_like(img)
	out[mask] = img[mask]
	patch = img[mask]

	# cv2.imwrite('Cropped.png', out)

	# converto image to grayscale
	img = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

	# sum each row and each volumn of the image
	sumOfCols = np.sum(img, axis=0)
	sumOfRows = np.sum(img, axis=1)

	# Find the first and last row / column that has a sum value greater than zero, 
	# which means its not all black. Store the found values in variables
	for i in range(len(sumOfCols)):
	        if sumOfCols[i] > 0:
	                x1 = i
	                # print('First col: ' + str(i))
	                break

	for i in range(len(sumOfCols)-1,-1,-1):
	        if sumOfCols[i] > 0:
	                x2 = i
	                # print('Last col: ' + str(i))
	                break

	for i in range(len(sumOfRows)):
	        if sumOfRows[i] > 0:
	                y1 = i
	                # print('First row: ' + str(i))
	                break

	for i in range(len(sumOfRows)-1,-1,-1):
	        if sumOfRows[i] > 0:
	                y2 = i
	                # print('Last row: ' + str(i))
	                break

	# create a new image based on the found values
	finalImage = out[y1:y2,x1:x2]
	while(1):
		cv2.imshow("1",finalImage)
		cv2.imwrite("./save_image/1.jpg", finalImage)
		k = cv2.waitKey(33)
		if k==27:    # Esc key to stop
		    break
		elif k==-1:  # normally -1 returned,so don't print it
		    continue
		else:
		    print (k) # else print its value
