# import networkx as nx
# import matplotlib.pyplot as plt
import random
import sys
random.seed()

adj_matrix = [] 
i_matrix = []
adj_list = []

# generator G(n, p)
# generator zależny od prawdopodobienstwa
# zwraca graf w postaci listy sąsiedztwa (bez wypisywaniea 1: )
# np:
# 3 4
# 3 4 5
# 1 2 5
# 1 2 5
# 2 3 4
def gen_G_p(n, p):
    # losuje niepowtarzalne wartosci (zeby nie losowac dwa razy czy moze byc np polaczenie 1-2 i 2-1)
    if type(n) is not int:
        print("Podana liczba wierzcgołków nie jest liczbą całkowitą")
        sys.exit()
    if p < 0 or p > 1:
        print("p musi być w przedziale <0, 1>")
        sys.exit()
    g_list = []
    for i in range(n):
        row = []
        for j in range(i, n):
            if random.random() < p and i != j:
                row.append(j + 1)
        g_list.append(row)

    # uzupelnienie o poprzednio wylosowane wartosci
    for i in range(1, n):
        for j in range(0, i):
            if i + 1 in g_list[j]:
                g_list[i].append(j + 1)

    for i in range(n):
        g_list[i].sort()

    return g_list

    # zapisywanie do pliku 
    # musi istnieć plik random_graph.txt
    # musi istnieć plik do korego ma zapisywać
    # with open("random_graph.txt", 'w') as file:
    #     file.writelines(' '.join(str(j) for j in i) + '\n' for i in g_list)
    # file.close()

#generator G(n, l) zwraca macierz sąsiedztwa
# np.
# 0 1 0 0 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 1 0 1
# 1 1 0 1 0
def gen_G_l(n, l):
    if type(n) is not int:
        print("Podana liczba wierzcgołków nie jest liczbą całkowitą")
        sys.exit()
    if type(l) is not int:
        print("Podana liczba krawędzi nie jest liczbą całkowitą")
        sys.exit()
    if l > ((n * (n - 1)) / 2) or l < 0:
        print("l musi być w przedziale <0, (n * (n - 1)) / 2>")
        sys.exit()
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    sum_1 = 0
    for i in range(n):
        for j in range(n):
            if sum_1 < l and j > i:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1 
                sum_1 += 1
    return adj_matrix


#funkcja tworząca plik txt na podstawie którego rysowany jest wykres
def create_file_to_draw(adj_list):
    with open('Adj.txt', 'r+') as file:
        for i in range(len(adj_list)):
            file.write(str(i+1) + ' ')
            for j in range(len(adj_list[i])):
                file.write(str(adj_list[i][j]) + ' ')
            file.write('\n')
        file.close()

#funkcja rysująca wykres
def draw_circular(adj_list):
    create_file_to_draw(adj_list)
    graph = nx.read_adjlist("Adj.txt", create_using=nx.Graph(), nodetype=int)
    print(nx.info(graph))

    options = {
        'node_color': '#424242',
        'node_size': 300,
        'line_color': '#878787',
        'font_color': '#f2f2f2',
        'width': 0.25,
        'with_labels': 1,
    }

    nx.draw_circular(graph, **options)
    # nx.draw(graph, **options)
    plt.show()

#wypisywanie listy sąsiedztwa
def print_list(adj_list):
    print("Wypisuję listę sąsiedztwa:")
    for i in range(len(adj_list)):
        print(i + 1, end = ': ', )
        if len(adj_list[i]) == 0:
            print()
        else:
            for j in range(len(adj_list[i]) - 1):
                print(adj_list[i][j], end = ', ')
            print(adj_list[i][len(adj_list[i]) - 1]) 
    print()

#wypisywanie macierzy
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()
    print()

#wypisywanie macierzy sąsiedztwa
def print_adj_matrix(adj_matrix):
    print("Wypisuję macierz sąsiedztwa:")
    print_matrix(adj_matrix)

#wypisywanie macierzy incydencji
def print_i_matrix(i_matrix):
    print("Wypisuję macierz incydencji:")
    print_matrix(i_matrix)

# funkcja transponująca macierz
def transpose(matrix):
    t_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix

#zmiana listy sąsiedztwa na macierz sąsiedztwa
def adj_list_to_adj_matrix(adj_list):
    adj_matrix = []
    for i in range(len(adj_list)):
        row = []
        for j in range(len(adj_list)):
            if j + 1 in adj_list[i]:
                row.append(1)
            else:
                row.append(0)
        adj_matrix.append(row)
    return adj_matrix

#zamiana listy na macierz incydencji
def adj_list_to_i_matrix(adj_list):
    adj_matrix = []
    i_matrix = []
    adj_matrix = adj_list_to_adj_matrix(adj_list)
    i_matrix = adj_matrix_to_i_matrix(adj_matrix)
    return i_matrix



#zmiana macierzy sąsiedztwa na listę sąsiedztwa
def adj_matrix_to_list(adj_matrix):
    adj_list = []
    for i in range(len(adj_matrix)):
        row = []
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                row.append(j + 1)

        adj_list.append(row)
    return adj_list

#zmiana macierzy sąsiedztwa na macierz incydencji
def adj_matrix_to_i_matrix(adj_matrix):
    t_i_matrix = []
    i_matrix = []
    number_of_edge = 0
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i > j and adj_matrix[i][j] == 1:
                number_of_edge += 1

    t_i_matrix = [[0 for _ in range(len(adj_matrix))] for _ in range(number_of_edge)]
    edge = 0

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i > j and adj_matrix[i][j] == 1:
                t_i_matrix[edge][i] = 1
                t_i_matrix[edge][j] = 1
                edge += 1

    i_matrix = transpose(t_i_matrix)
    return i_matrix

#zamiana macierze incydencji na macierz sąsiedztwa
def i_matrix_to_adj_matrix(i_matrix):
    adj_matrix = []
    t_i_matrix = transpose(i_matrix)
    adj_matrix = [[0 for _ in range(len(t_i_matrix[0]))] for _ in range(len(t_i_matrix[0]))]
    indexes = []

    for i in range(len(t_i_matrix)):
        indexes.clear()
        for j in range(len(t_i_matrix[0])):
            if t_i_matrix[i][j] == 1:
                indexes.append(j)
        if not len(indexes) == 0:
            for j in range(len(adj_matrix[0])):
                adj_matrix[indexes[0]][indexes[1]] = 1 
                adj_matrix[indexes[1]][indexes[0]] = 1 
    return adj_matrix         

#zamiana macierzy incydencji na listę sąsiedztwa
def i_matrix_to_list(i_matrix):
    adj_list = []
    adj_matrix = []
    adj_matrix = i_matrix_to_adj_matrix(i_matrix)
    adj_list = adj_matrix_to_list(adj_matrix)
    return adj_list


#zrobic weryfikzaje wprowadzanych danych
with open('FileIn.txt') as file:
    mode = str(file.readline().split()[0])
    for line in file:
        if mode == 'N':
            row = []
            for element in line.strip().split():
                row.append(int(element))
            adj_matrix.append(row)

        elif mode == 'I':
            row = []
            for element in line.strip().split():
                row.append(int(element))
            i_matrix.append(row)


        elif mode == 'L':
            row = []
            it = 0    
            for element in line.strip().split(' '):
                if it == 0:
                    it += 1
                else:
                    row.append(int(element))
            adj_list.append(row)

if mode == 'N':
    i_matrix = adj_matrix_to_i_matrix(adj_matrix)
    adj_list = adj_matrix_to_list(adj_matrix)

elif mode == 'I':
    adj_matrix = i_matrix_to_adj_matrix(i_matrix)
    adj_list = i_matrix_to_list(i_matrix)

elif mode == 'L':
    adj_matrix = adj_list_to_adj_matrix(adj_list)
    i_matrix = adj_list_to_i_matrix(adj_list)


###testowanie zad 1
print_list(adj_list)
print_adj_matrix(adj_matrix)
print_i_matrix(i_matrix)


### testowanie zad 2
# create_file_to_draw(adj_list)
# draw_circular(adj_list)


## testowanie zad 3 - prawdopodobieństwo
# adj_list = gen_G_p(6, 0.7)
# adj_matrix = adj_list_to_adj_matrix(adj_list)
# i_matrix = adj_list_to_i_matrix(adj_list)
# print_list(adj_list)
# print_adj_matrix(adj_matrix)
# print_i_matrix(i_matrix)


###testowanie zad 3 - krawedzie
# adj_matrix = gen_G_l(8, 8)
# i_matrix = adj_matrix_to_i_matrix(adj_matrix)
# adj_list = adj_matrix_to_list(adj_matrix)
# print_list(adj_list)
# print_adj_matrix(adj_matrix)
# print_i_matrix(i_matrix)






# W FileIn w pierwszej lini musimy podać co podajemy:
# N - macierz sąsiedztwa
# I - macierz incydencji
# L - listę sąsiedztwa
# macierze itd mają być bezpośrednio pod literką
# nie może być nigdzie pustych linii
# przykładowe pliki:
# L
# 1: 2 5
# 2: 1 3 4 5
# 3: 2 4
# 4: 2 3 5
# 5: 1 2 4

# N
# 0 1 0 0 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 1 0 1
# 1 1 0 1 0

# I
# 1 0 0 0 1 0 0
# 1 1 1 0 0 1 0
# 0 1 0 1 0 0 0
# 0 0 1 1 0 0 1
# 0 0 0 0 1 1 1