import networkx as nx  # Імпорт бібліотеки networkX для роботи з графами
import matplotlib.pyplot as plt  # Імпорт бібліотеки matplotlib для візуалізації графів

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
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()  # Ініціалізація множини відвіданих вершин
    visited.add(start)  # Додавання стартової вершини до відвіданих
    print(start, end=' ')  # Виведення поточної вершини
    for neighbor in graph[start]:  # Обхід сусідніх вершин
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)  # Рекурсивний виклик для сусідньої вершини

print("Обхід графа за допомогою DFS (рекурсивно):")
dfs_recursive(G, 'Station_A')
print()

# Пошук у ширину (BFS)
from collections import deque  # Імпорт deque для реалізації черги

def bfs_iterative(graph, start):
    visited = set()  # Ініціалізація множини відвіданих вершин
    queue = deque([start])  # Ініціалізація черги з стартовою вершиною
    while queue:
        vertex = queue.popleft()  # Витягуємо вершину з черги
        if vertex not in visited:
            print(vertex, end=' ')  # Виведення поточної вершини
            visited.add(vertex)  # Додавання вершини до відвіданих
            queue.extend(set(graph[vertex]) - visited)  # Додавання сусідніх вершин до черги

print("Обхід графа за допомогою BFS (ітеративно):")
bfs_iterative(G, 'Station_A')
print()
