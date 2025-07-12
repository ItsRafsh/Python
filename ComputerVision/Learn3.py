
import cv2
import numpy as np

image = np.zeros((500,500, 3), dtype='uint8')
# line
cv2.line(image, (50, 50), (450, 450), (0,255,0),thickness=3)
# 
# circle
cv2.circle(image,(250, 250),100, (255,255,255), thickness=3)

# rectangle(persegi) / shape
cv2.rectangle(image, (50,50),(450,450),(0,255,0),thickness=-1)

# polygon
# points = np.array([[150, 200],[250, 100], [350, 200]],np.int32)  bentuk segitiga
points = np.array([[150, 200],[250, 100], [350, 200], [250, 450]],np.int32)  #bentuk layang2
points = points.reshape(-1, 1, 2)
cv2.polylines(image, [points], isClosed=True, color=(255, 255, 0), thickness=3)
print(points)

# text
image = cv2.imread(r'foto1.png') #masih erroe cuyy
resized_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
cv2.putText(resized_image, 'gue bisa ngoding',(50, 50),cv2.FONT_HERSHEY_SIMPLEX, (255, 255, 255), thickness=3)

cv2.waitKey(0)
cv2.imshow('image new', camera)


# ---------- ini menampilkan KAMERA
camera = cv2.VideoCapture(0)
while True:
    sts, frame = camera.read()

    if not sts:
        break

    flipped_frame = cv2.flip(frame, 1) # yg frame ganti jadi flipped_frame


    cv2.line(frame, (50, 50), (250, 50), (255,255,255), thickness=2)
    # text = cv2.putText(frame, 'HELLO WORLD', (250,250), cv2.FONT_HERSHEY_PLAIN,3) jngn
    cv2.putText(frame, 'Live cam', (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), thickness=2)

    cv2.imshow('Live Camera', frame)
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

