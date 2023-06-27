import cv2
source ="iron man.jpeg"
destination = 'new_image.jpeg'
x = int(input("Enter the percent you want to change in image: "))
scale_percent = x;
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
#calculate the x percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# tuple
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)

cv2.waitKey(0)
