1. I don't understand about pip3, what's diffferent between pip3 vs package manager ubuntu
2. My perspective
	- mediapipe : tool develop by google, serve about detect & analyze object on Computer Vision
	- opencv-python : computer vison
	- tensorflow : tool develop by google, support build model relate Machine Learning, Deep Learning.
	
	
	



Note xử lý ảnh dùng Python + OpenCV

img = cv2.imread("path", color)   -  open image file

cv2.imshow("Title window", img)		- show image file on window

cv2.line(img, (0,0), (400, 300), (255,255,255) , 5);			-    draw a line
		obj   start    end         B  G   R     weigth
		
cv2.imwrite('output.jpg', img)     - save(if exist) or create a picture file
			 file name    obj

cv2.destroyAllWindows()            - close all windows

cv2.waitKey(0)					-   hold window until press any key to close
 

---------- thuoc tinh cua image ---------------

shapeVal = img.shape            :          shapeVal = (738, 602, 3) -> (dai, rong, 3 kenh mau RGB)
										   shapeVal = (738, 602)    ->  anh xam den(ko mau)
sizeVal  = img.size  			:			sizeVal = 4469800 (kB) 
typeVal  = img.dtype			:			typeVal = 'uint8'

subImage  = img[200:300, 400:500]  :      crop anh voi img[x_0 : y_0, x_1 : y_1]

newImgColor  = subImage[ : , : , 0]  	:	convert color of image	0 - blue, 1 - green, 2 - red 

------------ long 2 anh vao nhau ---------------
img1 = cv2.imread("", 1);
img2 = cv2.imread("", 1);
img3 = cv2.add(img1, img2)

------------- tach 1 object ra khoi image -----------
import numpy as np			???

img = np.uint8([[[232, 162, 0 ]]]);
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img2 = cv2.imread("path",1)								
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)			# convert RGB -> HSV
min_color = np.array([97, 255, 232])						# gioi han duoi
max_color = np.array([100, 255, 232])						# gioi han tren
mask = cv2.inRange(hsv_img2, min_color, max_color)			# object duoc loc ra co mau White, nen con lai mau Black
final = cv2.bitwise_and(img2, img2, mask= mask)				# toan tu * -> 1*0 = 0, giu lai object tren nen Black
cv2.waitKey(0);



-------------  Machine learning with Matplotlib library ---------------
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(4, 5, 150, 'b' , '<' )         			# x = 4, y = 5, size = 150, 'b' = blue , < = <|
plt.show()											# show ban do 

print(np.random.randint(0, 100, (4, 2)))			# random 0 - 100 , array co 4 phan tu, trong 4 phan tu co 2 phan tu con





-------------  Project detect ball project --------------------


_ , mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)    
cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

Find meaning findContours, threshold




