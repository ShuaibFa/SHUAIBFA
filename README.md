Image Processing Phase 1 project
Participants: Shuaib Faysal 17w0048 , Shaban Reda 1700683 , Farouk Atef 15x0045


In the project we used and applied Hough Transform in to take the image that we uploaded and change them into grayscale. 
In the python project lanes.ipynb we tried to get the matplotlib dimensions for the images but it didnt work so we kept on assumming our own dimensions until we got the right dimensions in the image. That was until we found a source which helped us get the right outlining for our image.



Detecting edges using color transforms, gradients and other methods, one of the important methods is sobel filter which gets the image gradient in x and y....First, define sobal filter function to take the input image and the range of pixels (def abs_sobel_thresh(img, orient='x', thresh_min=0, thresh_max=255)) applying the derivative(gradient) in x and y(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel) & cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)) axis then apply proper thershold and color thershold, then transform to the binary image 8_bit.


We didnt use camera callibration 
