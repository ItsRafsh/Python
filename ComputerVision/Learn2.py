import cv2

# melakukan rotated manual foto
image = cv2.imread(r'foto1.png')

# ---------------- resize
resized_image = cv2.resize(image, (500,500),interpolation=cv2.INTER_AREA)


# ---------------- rotate function
rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)



# ---------------- rotate manual
(h, w) = resized_image.shape[:2]
center = (w//2, h//2)

rotation_matriks = cv2.getRotationMatrix2D(center, -180, 1)     # mengatur putaran , rotation besaran, 0.1 paling kecil
rotated_image = cv2.warpAffine(resized_image, rotation_matriks, (w, h))



# ---------------- croping Image
cropped_image = resized_image[150:350, 150:350]



# ---------------- conversi warna gambar(default: BGR)
# grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
# hsv (hue, saturation, value) coba sendiri



# ---------------- flip
flip_hor = cv2.flip(resized_image,1)
flip_ver = cv2.flip(resized_image,0)
flip_both = cv2.flip(resized_image,-1)
cv2.imshow('hor', flip_hor)
cv2.imshow('ver', flip_ver)
cv2.imshow('both', flip_both)



# ---------------- PIXEL MANIPULATION
pixel = resized_image[100, 100]
# ubah warna pixel
resized_image[100:400, 100:400] = [0, 0, 255] # merah
cv2.imshow('warnaa', resized_image)


cv2.imshow('Gambar abu', gray_image) #warna jadi abu-abu
cv2.imshow('Gambar', cropped_image) 
cv2.imshow('Gambar normal', resized_image) #bisa lebih dari 1 foto ini line
cv2.waitKey(0)
cv2.destroyAllWindows()


# cara save
cv2.imwrite(r'foto_cropped.png', cropped_image)



