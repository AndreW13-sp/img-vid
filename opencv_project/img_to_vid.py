import cv2
import os

path = '/Users/swarajpanchal/Desktop/Img to vid/opencv_project/imgs/'
output_path = '/Users/swarajpanchal/Desktop/Img to vid/opencv_project/vid/'
output_video_name = 'sunset1.mp4'
output_video_full_path = output_path + output_video_name

pre_imgs = os.listdir(path)
# print(pre_imgs)
img = []

for i in pre_imgs:
    i = path+i 
    # print(i) 
    img.append(i)

# print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame = cv2.imread(img[0])
print(frame)
size = list(frame.shape)
print(frame.shape)
del size[2]
#size.reverse()
# print(size)

video = cv2.VideoWriter(output_video_full_path, cv2_fourcc, 1, size) #output: video name, fourcc, fps, size
counter = 0
for i in img:
    video.write(cv2.imread(i))
    print('frame', counter+1, 'of', len(img))
    counter+=1
video.release()