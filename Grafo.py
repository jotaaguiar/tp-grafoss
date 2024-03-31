from Lista import List
from Matriz import Matrix
import random
import time


def insertEdge(matrix: Matrix, list: List, directed):
    source = int(input("Vértice de origem: "))
    destination = int(input("Vértice de destino: "))
    weight = int(input("Peso da aresta (ou 1 para aresta não ponderada): "))

    # -----LISTA------
    list = list.add_edge(source, destination, weight, directed)

    # -----MATRIZ-----
    matrix = matrix.add_edge(source, destination, weight)


def removeEdge(matrix: Matrix, list: List, directed):
    source = int(input("Vértice de origem: "))
    destination = int(input("Vértice de destino: "))

    # -----LISTA------
    list = list.remove_edge(source, directed)

    # -----MATRIZ-----
    matrix = matrix.remove_edge(source, destination)


def printGraph(matrix: Matrix, list: List):
    print("-----LISTA------")
    print("Lista de Adjacência do Grafo:")
    print(list.graph)

    print("-----MATRIZ-----")
    print("Matriz de Adjacência do Grafo:")
    print(matrix)


def getVertexDegree(matrix: Matrix, list: List, directed):
    vert = int(input("Vértice que deseja consultar: "))
    print("-----LISTA------")
    degree = list.get_vertice_degree(vert, directed)
    if directed:
        print(f"O grau de entrada do vértice {vert} é {degree['Entry']}, e saída é {degree['Output']}")
    else:
        print(f"O grau do vertice {vert} é {degree}")

    print("-----MATRIZ-----")
    if matrix.digraph:
        degree = matrix.get_rate(vert, directed)
        print(f"O grau de entrada do vértice {vert} é {degree['entry']}, e saída é {degree['exit']}")
    else:
        degree = matrix.get_rate(vert)
        print(f"O grau do vertice {vert} é {degree['entry']}")


def getGraphDegree(matrix: Matrix, list: List, directed):
    print("-----LISTA------")
    degree = list.get_graph_degree(directed)
    if directed:
        print(f"O grau de entrada do grafo é {degree['Entry']}, e saída é {degree['Output']}")
    else:
        print(f"O grau do grafo é {degree}")

    print("-----MATRIZ-----")
    graphDegree = matrix.get_graphDegree()
    print(f"Grau do grafo (matriz): {graphDegree}")


def find_neighbors(matrix: Matrix, list: List, directed):
    vert = int(input("Qual o vértice que deseja: "))

    print("-----LISTA------")
    neighbors = list.get_vertice_neighborhood(vert, directed)
    if len(neighbors):
        print(f"Os vizinhos são: {neighbors}")
    else:
        print("Não há vizinhos")

    print("-----MATRIZ-----")
    neighbors = matrix.find_neighbors(vert)
    if len(neighbors):
        print(f"Os vizinhos são: {neighbors}")
    else:
        print("Não há vizinhos")


def is_connected(matrix: Matrix, list: List, directed):
    print("-----LISTA------")
    if list.is_connected():
        print("O grafo é conexo.")
    else:
        print("O grafo não é conexo.")

    print("-----MATRIZ-----")
    if not directed:
        if matrix.is_connected():
            print("O grafo é conexo.")
        else:
            print("O grafo não é conexo.")
    else:
        if matrix.is_strongly_connected():
            print("O grafo é fortemente conectado.")
        else:
            print("O grafo não é fortemente conectado.")


def is_regular(matrix: Matrix, list: List, directed):
    print("-----LISTA------")
    if list.is_regular():
        print("O grafo é regular.")
    else:
        print("O grafo não é regular.")

    print("-----MATRIZ-----")
    if matrix.is_regular():
        print("O grafo é regular.")
    else:
        print("O grafo não é regular.")


def is_complete(matrix: Matrix, list: List, directed):
    print("-----LISTA------")
    if list.is_complete():
        print("O grafo é completo.")
    else:
        print("O grafo não é completo.")

    print("-----MATRIZ-----")
    if matrix.is_complete():
        print("O grafo é completo.")
    else:
        print("O grafo não é completo.")



if __name__ == "__main__":
    directed = bool(int(input("O grafo será direcionado? (1- Direcionado / 0- Não direcionado): ")))
    n = int(input("Informe o número de vértices: "))
    list = List(n)
    matrix = Matrix(n, directed)

    while True:
        print("\nOpções:")
        print("1. Inserir aresta")
        print("2. Remover aresta")
        print("3. Mostrar grafo")
        print("4. Consultar grau do vértice")
        print("5. Consultar grau do grafo")
        print("6. Consultar vizinhos de um vértice")
        print("7. Verificar se o grafo é conexo")
        print("8. Verificar se o grafo é regular")
        print("9. Verificar se o grafo é completo")


        choice = int(input("Escolha uma opção: "))

        match choice:
            case 1:
                insertEdge(matrix, list, directed)
            case 2:
                removeEdge(matrix, list, directed)
            case 3:
                printGraph(matrix, list)
            case 4:
                getVertexDegree(matrix, list, directed)
            case 5:
                getGraphDegree(matrix, list, directed)
            case 6:
                find_neighbors(matrix, list, directed)
            case 7:
                is_connected(matrix, list, directed)
            case 8:
                is_regular(matrix, list, directed)
            case 9:
                is_complete(matrix, list, directed)