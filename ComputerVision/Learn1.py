import os

import cv2.data
os.system('cls')

import cv2



# untuk foto di file
image = cv2.imread(r'foto1.png')
if image is None:
    print('gambar ga ditemukan')
else:
    resized_image = cv2.resize(image, (500,500), interpolation=cv2.INTER_AREA)  #interpolsi biar HD

    cv2.imshow('foto rafa',resized_image)
    cv2.waitKey(0) # 2 buah indikator,   1.delay 2. mencet tombol
    # 0 delay time special : forever
    cv2.destroyAllWindows()



# untuk video di file
video = cv2.VideoCapture(r'video1.mp4')
while True:
    status, frame = video.read()    #status = true, jika ada frame yg diambil
    
    if not status:
        break
    resized_image = cv2.resize(frame, (500,500), interpolation=cv2.INTER_AREA)  #interpolsi biar HD
    
    cv2.imshow('Video Rafa', resized_image)
    if cv2.waitKey(20) & 0xFF == ord('q'):    #bitwise operation
        break
video.release()
cv2.destroyAllWindows()



# menampilkan kamera laptop
camera = cv2.VideoCapture(0)
while True:
    status, frame = camera.read()
    if not status:
        break

    mirror = cv2.flip(frame, 1)

    cv2.imshow('CAMERA', mirror)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

