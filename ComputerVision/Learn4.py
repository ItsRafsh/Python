

import cv2
image = cv2.imread(r'foto1.png')

resized_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
_, threshold = cv2.threshold(resized_image, 122, 255, cv2.THRESH_BINARY)

cv2.imshow('gambar gw', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#  untuk membuat kotak yg muncul di foto wajah 
image = cv2.imread(r'foto2.png')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

resized_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in face:
    cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255,0,0), thickness=3)

cv2.imshow('THRESHOLD', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#  untuk membuat kotak yg muncul di video yg ada di file 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(r'video1.mp4')

while True:
    status, frame = video.read()

    if not status:
        break

    resized_video = cv2.resize(frame, (500,500), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized_video, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    for (x, y, w, h) in face:
        cv2.rectangle(resized_video, (x, y), (x+w, y+h), (255,0,0), thickness=3)

    cv2.imshow('Camera video', resized_video)
    if cv2.waitKey(15) % 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



#  untuk membuat kotak yg muncul di video live wajah 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

while True:
    status, frame = camera.read()

    if not status:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), thickness=3)
        cv2.putText(frame, 'terdeteksi anak lelah', (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0,128,0), thickness=5)

    cv2.imshow('Camera video', frame)
    if cv2.waitKey(15) % 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

