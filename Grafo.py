from Lista import List
from Matriz import Matrix
import random
import time


class Subconjunto:
    def __init__(self, pai, classificacao):
        self.pai = pai
        self.classificacao = classificacao


class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso
        

# Função para verificar se o grafo é bipartido
def is_bipartite(graph):
    colors = {}  # Dicionário para armazenar as cores dos vértices
    stack = []  # Pilha para realizar a DFS

    # Função auxiliar para atribuir cores durante a DFS
    def dfs(node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        for neighbor, _ in graph.graph.get(node, []):
            if not dfs(neighbor, 1 - color):  # Alternar as cores entre 0 e 1
                return False
        return True

    # Realiza a DFS para todos os vértices não visitados
    for node in graph.graph:
        if node not in colors:
            if not dfs(node, 0):
                return False
    return True

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


def depth_first_search(matrix: Matrix, list: List):
    vert = int(input("Informe o vértice de partida para a busca em profundidade: "))
    print("-----LISTA------")
    search = list.dfs(vert)
    if len(search):
        print(f"Resultado da busca: {search}")
    else:
        print("Nada encontrado")

    print("-----MATRIZ-----")
    matrix.depth_first_search(vert)


def breadth_first_search(matrix: Matrix, list: List):
    vert = int(input("Informe o vértice de partida para a busca em largura: "))
    print("-----LISTA------")
    list.bfs(vert)

    print("-----MATRIZ-----")
    print(f"Vertices visitados: {matrix.bfs(vert)}")


def get_path(matrix: Matrix, list: List, directed):
    source = int(input("Vértice de origem: "))
    destination = int(input("Vértice de destino: "))
    print("-----LISTA------")
    path = list.get_path(source, destination)
    if path != []:
        print("Há o caminho: ")
        print(path)
    else:
        print("Não há caminho")

    print("-----MATRIZ-----")
    if not matrix.get_Path(source, destination):
        print("Não há caminho")
        
        
def autofill(matrix: Matrix, list: List):
    for i in range(len(list.graph)):
        for j in range(len(list.graph)):
            if random.random() < 0.3:
                weight = random.randint(1, 10)
                list.add_edge(i, j, weight, directed)
                matrix.add_edge(i, j, weight)
                
def bipartido(matrix: Matrix, list_obj: List):

    # Verificar se o grafo é bipartido
    if is_bipartite(list_obj):
        print("O grafo é bipartido.")
    else:
        print("O grafo não é bipartido.")
        
def is_simple(graph: Matrix) -> bool:
    for i in range(graph.n):
        for j in range(graph.n):
            if graph.graph[i][j] != "-" and i == j:  # Se há um laço
                return False
            for k in range(graph.n):
                if graph.graph[i][j] != "-" and graph.graph[j][k] != "-" and graph.graph[i][k] != "-":  # Se há uma aresta paralela
                    return False
    return True
 
def simpleGraph(matrix: Matrix):
    # Verificar se o grafo é simples
    if is_simple(matrix):
        print("O grafo é simples.")
    else:
        print("O grafo não é simples.")
        
def encontrar(subconjuntos, i):
    if subconjuntos[i].pai != i:
        subconjuntos[i].pai = encontrar(subconjuntos, subconjuntos[i].pai)
    return subconjuntos[i].pai


def unir(subconjuntos, x, y):
    raiz_x = encontrar(subconjuntos, x)
    raiz_y = encontrar(subconjuntos, y)

    if subconjuntos[raiz_x].classificacao < subconjuntos[raiz_y].classificacao:
        subconjuntos[raiz_x].pai = raiz_y
    elif subconjuntos[raiz_x].classificacao > subconjuntos[raiz_y].classificacao:
        subconjuntos[raiz_y].pai = raiz_x
    else:
        subconjuntos[raiz_y].pai = raiz_x
        subconjuntos[raiz_x].classificacao += 1


def encontrar_AGM(matrixx=None):


    if matrixx is not None:
        matrix = matrixx.graph
        n = len(matrix)
        arestas = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != "-" and i != j:
                    arestas.append(Aresta(i, j, int(matrix[i][j])))

        agm = []
        subconjuntos = []

        arestas.sort(key=lambda x: x.peso)

        for i in range(n):
            subconjuntos.append(Subconjunto(i, 0))

        i = 0
        while len(agm) < n - 1 and i < len(arestas):
            aresta = arestas[i]

            raiz_origem = encontrar(subconjuntos, aresta.origem)
            raiz_destino = encontrar(subconjuntos, aresta.destino)

            if raiz_origem != raiz_destino:
                agm.append(aresta)
                unir(subconjuntos, raiz_origem, raiz_destino)

            i += 1

        print("Arestas da Árvore Geradora Mínima:")
        for aresta in agm:
            print(f"{aresta.origem} -- {aresta.destino} (peso {aresta.peso})")

def topological_sort(graph):
    stack = []

    # Função auxiliar DFS para fazer a ordenação topológica
    def dfs(node, visited, stack):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)

    visited = set()
    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)

    return stack[::-1]


def topological_sortWrapper(matrix: Matrix, list: List , directed : bool):
    if directed == False:
        print("Não é possível realizar a ordenação topologica, por se tratar de um grafo não direcionado. ")
        
        return True
    
    if matrix is not None:
        # Convertendo a matriz de adjacência para um dicionário
        graph_dict = {}
        for i in range(matrix.n):
            neighbors = []
            for j in range(matrix.n):
                if matrix.graph[i][j] != "-":
                    neighbors.append(j)
            graph_dict[i] = neighbors

        # Ordenação topológica
        sorted_nodes = topological_sort(graph_dict)
        print("Ordenação Topológica (Matriz de Adjacência):", sorted_nodes)

    if list is not None:
        # Utilize a função topological_sort diretamente para a lista de adjacência
        sorted_nodes = topological_sort(list.graph)
        print("Ordenação Topológica (Lista de Adjacência):", sorted_nodes)
   
        
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
        print("7. Verificar se o grafo é simples")
        print("8. Verificar se o grafo é regular")
        print("9. Verificar se o grafo é completo")
        print("10. Verificar se o grafo é bipartido")
        print("11. Busca em profundidade")
        print("12. Busca em largura")
        print("13. Verificar se há caminho")
        print("14. Verificar se o grafo é conexo")
        print("15. Busca em AGM ( Kruskal )")
        print("16. Ordenação Topológica")
        print("17. Preencher automaticamente")


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
                simpleGraph(matrix)
            case 8:
                is_regular(matrix, list, directed)
            case 9:
                is_complete(matrix, list, directed)
            case 10:
                bipartido(matrix, list)
            case 11:
                depth_first_search(matrix, list)
            case 12:
                breadth_first_search(matrix, list)
            case 13:
                get_path(matrix, list, directed)              
            case 14:
                is_connected(matrix, list, directed)
            case 15:
                encontrar_AGM(matrix)
            case 16:
                topological_sortWrapper(matrix, list, directed)
            case 17:
                autofill(matrix, list)
