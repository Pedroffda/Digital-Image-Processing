import cv2
import numpy as np

# Carrega a imagem e converte para escala de cinza
img = cv2.imread('images/engrenagens_without_edge.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Inverte a escala de cinza (engrenagens pretas em fundo branco)
gray = cv2.bitwise_not(gray)

# Aplica filtro de mediana para evitar ruidos na imagem
gray = cv2.medianBlur(gray, 5)

# Encontra os contornos na imagem
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Para cada contorno encontrado, aplica a transformada de Hough circular para contar os dentes
for i, contour in enumerate(contours):
    # Cria uma máscara para extrair a engrenagem atual
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)
    engrenagem = cv2.bitwise_and(gray, mask)
    
    # Aplica a transformada de Hough circular para detectar os dentes da engrenagem
    circles = cv2.HoughCircles(engrenagem, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=5, maxRadius=50)
    num_dentes = 0
    if circles is not None:
        num_dentes = len(circles[0])
    
    # Pinta a área da engrenagem de branco se houver mais de um dente
    if num_dentes > 1:
        cv2.drawContours(img, [contour], -1, (255, 255, 255), -1)
    
    # # Desenha o número de dentes na engrenagem atual na imagem original
    # if num_dentes > 0:
    #     cv2.putText(img, str(num_dentes), tuple(contour[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
# Exibe a imagem com os contornos detectados e o número de dentes de cada engrenagem
cv2.imwrite('images/engrenagens_without_overlapping.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
