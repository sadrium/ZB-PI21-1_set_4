import threading


def print_matrix(matrix):
    for line in matrix:
        for elem in line:
            print('{}'.format(elem), end='\t')
        print()

def mult(X, Y):
    result = [[0] * 3]
    for z in range(len(Y[0])):
        for k in range(len(Y)):
            result[0][z] += X[0] * Y[k][z]
    print_matrix(result)

def write_result(matrix):
    file = open('result.txt', 'w')
    for i in range(matrix):
        for j in range(matrix[i]):
            file.write(matrix[i][j] + ' ')
        file.write('\n')

with open('matrix1.txt') as f:
    X = [[int(num) for num in line.split()] for line in f]

with open('matrix2.txt') as f:
    Y = [[int(num) for num in line.split()] for line in f]


print_matrix(X)
print_matrix(Y)

threads = list()
for i in range(len(X[0])):
    thr = threading.Thread(target=mult, args=(X[i], Y))
    threads.append(thr)
    thr.start()

for index, thread in enumerate(threads):
    thread.join()
