import cv2

# Carrega a imagem em escala de cinza
img = cv2.imread('images/teste2.png', 0)

# Aplica o método de Otsu para calcular o threshold
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Mostra a imagem original e a imagem binarizada
cv2.imwrite('images/ImagemOriginal.png', img)
cv2.imwrite('images/ImagemBinarizada.png', thresh)