size = int(input("Укажите размер матрицы(больше 4): "))
if size <= 4:
    quit()
matrix = [[' ' for i in range(size)] for j in range(size)]
matrix[0], matrix[size - 1] = [0 for i in range(size)], [0 for i in range(size)]
for i in range(size):
    matrix[i][0] = 0
for i in range(size):
    matrix[i][size - 1] = 0
radius = int(input("Укажите радиус: "))
if radius * 2 > size - 2:
    quit()
center_x = size // 2
center_y = size // 2
start_x, end_x = center_x - radius, center_x + radius
start_y, end_y = center_y - radius, center_y + radius
for i, j in zip(range(start_x, center_x + 1), range(center_y, start_y - 1, -1)):
    matrix[j][i] = 1
for i, j in zip(range(center_x, end_x + 1), range(start_y, center_y + 1)):
    matrix[j][i] = 1
for i, j in zip(range(end_x, center_x - 1, -1), range(center_y, end_y + 1)):
    matrix[j][i] = 1
for i, j in zip(range(center_x, start_x - 1, -1), range(end_y, center_y - 1, -1)):
    matrix[j][i] = 1
for i in range(center_y, center_y + 6):
    for j in range(center_x, center_x + 7):
        if i == center_y and j in [center_x + 1, center_x + 2, center_x + 4, center_x + 5] :
            matrix[i][j] = 2
        elif i == center_y + 1 and j in [center_x, center_x + 3, center_x + 6]:
            matrix[i][j] = 2
        elif i == center_y + 2 and j in [center_x + 1, center_x + 5]:
            matrix[i][j] = 2
        elif i == center_y + 3 and j in [center_x + 2, center_x + 4]:
            matrix[i][j] = 2
        elif i == center_y + 4 and j in [center_x + 3]:
            matrix[i][j] = 2
for i in range(size):
    print(*matrix[i])
