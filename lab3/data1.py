import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Зчитуємо датасет з файлу
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [list(map(int, line.split())) for line in lines]
        return np.array(points)

# Знаходимо опуклу оболонку
def find_convex_hull(points):
    hull = ConvexHull(points)
    return hull
# Зберігти новий датасет
def save_convex_hull_dataset(file_path, convex_hull_dataset):
    with open(file_path, 'w') as file:
        for point in convex_hull_dataset.simplices:
            file.write(f"{point[0]} {point[1]}\n")

# Встановлюємо розміри вікна
canvas_size = (960, 540)

# Відображаємо опуклу оболонку та точки
def plot_convex_hull(points, hull):
    plt.figure(figsize=(canvas_size[0]/80, canvas_size[1]/80))
    plt.scatter(points[:,1], points[:,0], c='red', label='Точки')
    for point in hull:
        plt.plot(points[point, 1], points[point, 0], 'b-')
    plt.title('Опукла оболонка')
    plt.legend()
    plt.xlim(0, canvas_size[0])
    plt.ylim(0, canvas_size[1])
    plt.savefig('convex_hull_plot.png')
    plt.show()

# Зчитуємо датасет
dataset = read_dataset('DS7.txt')

# Знаходимо опуклу оболонку
hull = find_convex_hull(dataset)

# Зберігаємо датасет опуклої оболонки
save_convex_hull_dataset("DS7_hull.txt", hull)

# Зчитуємо датасет
hull = read_dataset("DS7_hull.txt")

# Відображаємо та зберігаємо результат
plot_convex_hull(dataset, hull)
