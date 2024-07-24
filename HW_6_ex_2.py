import networkx as nx  # Імпорт бібліотеки networkX для роботи з графами
import matplotlib.pyplot as plt  # Імпорт бібліотеки matplotlib для візуалізації графів
from collections import deque  # Імпорт deque для реалізації черги в BFS

# Створення графа
G = nx.Graph()

# Додавання вузлів (станцій) та ребер (доріг) з вагами (відстанями в км)
edges = [
    ("Station_A", "Station_B", 5),
    ("Station_A", "Station_C", 7),
    ("Station_B", "Station_D", 3),
    ("Station_B", "Station_E", 4),
    ("Station_C", "Station_F", 2),
    ("Station_D", "Station_E", 6),
    ("Station_E", "Station_F", 3),
    ("Station_E", "Station_G", 8),
    ("Station_F", "Station_G", 5),
]

# Додавання ребер до графа з зазначенням ваги кожного ребра
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Візуалізація графа
pos = nx.spring_layout(G)  # Розташування вузлів графа
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12)  # Малювання графа
labels = nx.get_edge_attributes(G, 'weight')  # Отримання ваг ребер
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Додавання ваг до ребер на графіку
plt.title("Транспортна мережа міста")  # Назва графіку
plt.show()  # Показ графіку

# Кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

# Ступінь кожної вершини
degrees = dict(G.degree())
print("Ступінь кожної вершини:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Середній ступінь вершини
avg_degree = sum(degrees.values()) / num_nodes
print(f"Середній ступінь вершини: {avg_degree:.2f}")

# Чи є граф зв'язним
is_connected = nx.is_connected(G)
print(f"Чи є граф зв'язним: {is_connected}")

# Пошук у глибину (DFS)
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]  # Використовуємо стек для зберігання шляху
    while stack:
        (vertex, path) = stack.pop()  # Витягуємо вершину та шлях зі стеку
        for next in set(graph[vertex]) - set(path):  # Обхід сусідніх вершин, яких немає в поточному шляху
            if next == goal:
                yield path + [next]  # Повертаємо шлях, якщо досягли мети
            else:
                stack.append((next, path + [next]))  # Додаємо вершину та оновлений шлях до стеку

# Пошук у ширину (BFS)
def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])  # Використовуємо чергу для зберігання шляху
    while queue:
        (vertex, path) = queue.popleft()  # Витягуємо вершину та шлях з черги
        for next in set(graph[vertex]) - set(path):  # Обхід сусідніх вершин, яких немає в поточному шляху
            if next == goal:
                yield path + [next]  # Повертаємо шлях, якщо досягли мети
            else:
                queue.append((next, path + [next]))  # Додаємо вершину та оновлений шлях до черги

start_node = "Station_A"
goal_node = "Station_G"

# Отримання всіх шляхів з використанням DFS
dfs_result = list(dfs_paths(G, start_node, goal_node))
print("Шляхи з використанням DFS:")
for path in dfs_result:
    print(path)

# Отримання всіх шляхів з використанням BFS
bfs_result = list(bfs_paths(G, start_node, goal_node))
print("Шляхи з використанням BFS:")
for path in bfs_result:
    print(path)