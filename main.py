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
for row in range(center_y - 3, center_y + 3):
    for col in range(center_x - 3, center_x + 4):
        if row == center_y - 3 and center_x - col % 3 != 0 or row == center_y - 2 and center_x - col % 3 == 0 or row - col == 2 or row + col == center_x + 4:
            matrix[row][col] = 2
for i in range(size):
    print(*matrix[i])
