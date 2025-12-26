import math
from collections import Counter

def euclidean_distance(point1, point2):
    #Евклидово расстояние между двумя точками
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def knn_predict(train_data, train_labels, new_point, k=3):
    
    #train_data: список точек [[x1, y1], [x2, y2], ...]
    #train_labels: список меток [0, 1, 0, ...]
    #new_point: новая точка [x, y]
    #k: количество соседей
    
    # 1. Вычисляем расстояния до всех точек
    distances = []
    for i, point in enumerate(train_data):
        dist = euclidean_distance(point, new_point)
        distances.append((dist, train_labels[i]))
    
    # 2. Сортируем по расстоянию
    distances.sort(key=lambda x: x[0])
    
    # 3. Берем k ближайших
    k_nearest = distances[:k]
    
    # 4. Считаем голоса
    votes = [label for _, label in k_nearest]
    
    # 5. Выбираем самый частый класс
    most_common = Counter(votes).most_common(1)[0][0]
    
    return most_common

# Пример
# Обучающие данные: первая цифра - x, вторая - y, метка - класс
train_points = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 7], [8, 6]]
train_labels = [0, 0, 0, 1, 1, 1]  # 0 - красные, 1 - синие

# Новая точка для классификации
new_point = [4, 4]

# Предсказание
prediction = knn_predict(train_points, train_labels, new_point, k=3)
print(f"Новая точка {new_point} относится к классу: {prediction}")
print("(0 = красный, 1 = синий)")