def area(x1, y1, x2, y2, x3, y3):
    #Вычисление площади треугольника
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def is_point_in_triangle(px, py, ax, ay, bx, by, cx, cy):
    #Проверка точки в треугольнике
    # Площадь основного треугольника
    ABC = area(ax, ay, bx, by, cx, cy)
    
    # Площади маленьких треугольников
    PBC = area(px, py, bx, by, cx, cy)
    APC = area(ax, ay, px, py, cx, cy)
    ABP = area(ax, ay, bx, by, px, py)
    
    # Сравнение с небольшой погрешностью
    return abs(ABC - (PBC + APC + ABP)) < 0.000001

# Пример
A = (0, 0)
B = (5, 0)
C = (0, 5)
P = (1, 1)

result = is_point_in_triangle(P[0], P[1], A[0], A[1], B[0], B[1], C[0], C[1])
print(f"Точка {P} в треугольнике {A}{B}{C}: {result}")