matrix = []

while True:
    row = input()
    if row == 'end':
        break
    line = list(map(int, row.split()))
    matrix.append(line)

rows = len(matrix)
cols = len(matrix[0])

result = []

for i in range(rows):
    result_row = []
    for j in range(cols):
        top = matrix[(i - 1) % rows][j]
        bottom = matrix[(i + 1) % rows][j]
        left = matrix[i][(j - 1) % cols]
        right = matrix[i][(j + 1) % cols]

        result_row.append(top + bottom + left + right)
    result.append(result_row)

for rows in result:
    print(rows)