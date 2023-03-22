import cv2
import numpy as np

img = cv2.imread("images/ImagemBinarizada.png", 0)

adj = 4 # 4 para adj-8, 8 para adj-m

visited = [[False for col in range(img.shape[0])] for row in range(img.shape[1])]

dx = [0,  0, 1, -1, 1,  1, -1, -1]
dy = [1, -1, 0,  0, 1, -1,  1, -1]

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
			if(n_x < 0 or n_x >= img.shape[0] or n_y < 0 or n_y >= img.shape[1]):
				continue
			if(img[n_x, n_y] != 255 and not visited[n_x][n_y]):
				img[n_x, n_y] = 255
				st.append((n_x, n_y))

def clearEdge(img):
	# percorrer a borda superior
	for x in range(img.shape[1]):
		if img[0, x] == 0 and not visited[0][x]:
			print("Pixel preto encontrado na borda superior")
			dfs(0, x)
	# percorrer a borda direita
	for y in range(img.shape[0]):
		if img[y, img.shape[1]-1] == 0 and not visited[y][img.shape[1]-1]:
			print("Pixel preto encontrado na borda direita")
			dfs(y, img.shape[1]-1)
	# percorrer a borda inferior
	for x in range(img.shape[1]-1, -1, -1):
		if img[img.shape[0]-1, x] == 0 and not visited[img.shape[0]-1][x]:
			print("Pixel preto encontrado na borda inferior")
			dfs(img.shape[0]-1, x)
	# percorrer a borda esquerda
	for y in range(img.shape[0]-1, -1, -1):
		if img[y, 0] == 0 and not visited[y][0]:
			print("Pixel preto encontrado na borda esquerda")
			dfs(y, 0)

clearEdge(img)

cv2.imwrite("images/engrenagens_without_edge.png", img)
