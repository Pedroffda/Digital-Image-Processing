# Importação das bibliotecas necessárias
import cv2
import numpy as np

# Variável para contar quantas engrenagens foram encontradas
count = 1

# Leitura da imagem
img = cv2.imread('images/engrenagens_without_edge.png')

# Conversão da imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica um filtro de suavização para remover ruídos
gray = cv2.medianBlur(gray, 5)

# Detecta as bordas na imagem usando o algoritmo de detecção de bordas de Canny
edges = cv2.Canny(gray, 50, 200, apertureSize=3)

# Detecta linhas na imagem usando o algoritmo de transformada de Hough probabilística
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=10)

# Verifica se linhas foram detectadas na imagem
if lines is not None:
    # Loop pelas linhas detectadas
    for line in lines:
        x1, y1, x2, y2 = line[0]

# Encontra os contornos (bordas fechadas) na imagem
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop pelos contornos encontrados
for i, contour in enumerate(contours):
    # Aproxima o contorno por um polígono de menor número de lados
    approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
    
    # Verifica se o polígono tem pelo menos 16 vértices, o que indica que pode ser uma engrenagem
    if len(approx) >= 16:
        for vertex in approx:
            x, y = vertex[0]
        # Encontra o retângulo mínimo que envolve o contorno (pode ser uma engrenagem inclinada)
        rect = cv2.minAreaRect(contour)
        # Calcula a área do retângulo
        area = rect[1][0] * rect[1][1]
        # Escreve um texto indicando que a engrenagem foi aceita
        cv2.putText(img, str(count) + ": ACEITO", (approx[0][0][0]-100, approx[0][0][1]+380), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)
        count += 1
    else:
        # Se o polígono não tem pelo menos 16 vértices, é considerado indefinido
        # Escreve um texto indicando que a engrenagem é indefinida
        cv2.putText(img, "INDEFINIDO", (approx[0][0][0]-100, approx[0][0][1]+380), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)

# Salva a imagem com os resultados
cv2.imwrite('images/engrenagens_without_damage.png', img)

# Espera por uma tecla ser pressionada e fecha todas as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
