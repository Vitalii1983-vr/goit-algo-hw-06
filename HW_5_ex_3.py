import networkx as nx
import matplotlib.pyplot as plt

# Створення графа для транспортної мережі міста
G = nx.Graph()

# Додавання вузлів (станцій)
stations = [
    "Station_A", "Station_B", "Station_C",
    "Station_D", "Station_E", "Station_F", "Station_G"
]
G.add_nodes_from(stations)

# Додавання ребер з вагами (відстань між станціями)
edges = [
    ("Station_A", "Station_B", 5),
    ("Station_A", "Station_C", 2),
    ("Station_B", "Station_D", 4),
    ("Station_B", "Station_E", 11),
    ("Station_C", "Station_F", 8),
    ("Station_D", "Station_E", 2),
    ("Station_E", "Station_G", 3),
    ("Station_F", "Station_E", 1),
    ("Station_F", "Station_G", 6)
]

G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_color="black", font_weight="bold", width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста з вагами")
plt.show()

# Функція для реалізації алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)
    previous_nodes = {vertex: None for vertex in graph}
    
    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        # Якщо найменша відстань є нескінченністю, ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        # Оновлення відстаней до сусідніх вершин
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
        
        # Видалення поточної вершини з множини невідвіданих
        unvisited.remove(current_vertex)
    
    return distances, previous_nodes

# Функція для відновлення шляху від start до goal
def get_shortest_path(previous_nodes, start, goal):
    path = []
    current_vertex = goal
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]
    path = path[::-1]  # Зворотній порядок
    return path

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів від кожної вершини
for start in stations:
    distances, previous_nodes = dijkstra(G, start)
    print(f"Найкоротші відстані від {start}: {distances}")
    for goal in stations:
        if start != goal:
            path = get_shortest_path(previous_nodes, start, goal)
            print(f"Найкоротший шлях від {start} до {goal}: {path}")
