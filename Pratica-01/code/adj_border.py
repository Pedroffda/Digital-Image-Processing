from PIL import Image

img = Image.open("PDI/folha.png").convert('L')

adj = 8 # 4 para adj-8, 8 para adj-m

visited = [[False for col in range(img.height)] for row in range(img.width)]

dx = [0,  0, 1, -1, 1,  1, -1, -1]
dy = [1, -1, 0,  0, 1, -1,  1, -1]

def isEdge(x, y):
	for i in range(adj):
		if(img.getpixel((x + dx[i], y + dy[i])) == 0):
			return True
	return False

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
            # verifica se os pixels adjacentes sao validos
			if(x + dx[i] < 0 or x + dx[i] >= img.width or y + dy[i] < 0 or y + dy[i] >= img.height):
				continue

            # se a imagem for branca e estiver na borda
			if(img.getpixel((x + dx[i], y + dy[i])) == 255 and isEdge(x + dx[i], y + dy[i])):
				st.append((x + dx[i], y + dy[i]))
                # pinta o pixel de cinza
				img.putpixel((x + dx[i], y + dy[i]), 128)

for i in range(img.width):
	for j in range(img.height):
		if(visited == True):
			continue
		if(img.getpixel((i, j)) == 255):
			dfs(i, j)
		visited[i][j] = True

for i in range(img.width):
	for j in range(img.height):
		if(img.getpixel((i, j)) == 255):
			img.putpixel((i, j), 0)
		elif(img.getpixel((i, j)) == 128):
			img.putpixel((i, j), 255)

img.save("adjacenciam.png")
