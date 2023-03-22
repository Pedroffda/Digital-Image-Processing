from PIL import Image
import matplotlib.pyplot as plt

# abrir a imagem
img = Image.open("images/ImagemBinarizada.png").convert('L')
# img = Image.open("images/ImagemBinarizada.png")
adj = 4 # 4 para adj-8, 8 para adj-m

visited = [[False for col in range(img.height)] for row in range(img.width)]

dx = [0,  0, 1, -1, 1,  1, -1, -1]
dy = [1, -1, 0,  0, 1, -1,  1, -1]

# obter as dimensões da imagem
width, height = img.size

def dfs(i, j):
	st = [(i, j)]
	while(len(st) > 0):
		pixel = st.pop()
		x = pixel[0]
		y = pixel[1]
		if(visited[x][y]):
			continue
		visited[x][y] = True
		for i in range(adj):

			n_x = x + dx[i]
			n_y = y + dy[i]
            # verifica se os pixels adjacentes sao validos
			if(n_x < 0 or n_x >= img.width or n_y < 0 or n_y >= img.height):
				continue

            # se a cor do pixel for preto
			if(img.getpixel((n_x, n_y)) != 255 and not visited[n_x][n_y]):
				img.putpixel((n_x, n_y), 255)
				st.append((n_x, n_y))

def clearEdge(img):
	# percorrer a borda superior
	for x in range(width):
		if img.getpixel((x, 0)) == 0 and not visited[x][0]:
			print("Pixel preto encontrado na borda superior")
			dfs(x,0)
	# percorrer a borda direita
	for y in range(height):
		if img.getpixel((width-1, y)) ==  0 and not visited[width-1][y]:
			print("Pixel preto encontrado na borda direita")
			dfs(width-1,y)
	# percorrer a borda inferior
	for x in range(width-1, -1, -1):
		if img.getpixel((x, height-1)) == 0 and not visited[x][height-1]:
			print("Pixel preto encontrado na borda inferior")
			dfs(x, width-1)
	# percorrer a borda esquerda
	for y in range(height-1, -1, -1):
		if img.getpixel((0, y)) == 0 and not visited[0][y]:
			print("Pixel preto encontrado na borda esquerda")
			dfs(0, y)

clearEdge(img)

img.save("images/engrenagens_without_edge.png")