import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Зчитування датасету з файлу
data = np.loadtxt('dataset.txt')[:, ::-1]  # Переставляємо колонки y і x місцями

# Розділення датасету на зв'язані області
vor = Voronoi(data, qhull_options='Qc Qz')  # Зберігаємо Qc та Qz, але видаляємо Qbb

# Знаходження центрів ваги зв'язаних областей
centers = np.array([np.mean(vor.vertices[region], axis=0) for region in vor.regions if -1 not in region and len(region) > 0])

# Будування діаграми Вороного
fig, ax = plt.subplots(figsize=(12, 6))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='gray', line_width=0.5)

# Встановлення розмірів вікна
plt.xlim([0, 960])
plt.ylim([0, 540])

# Відображення центрів ваги кругами діаметром 5 пкс
ax.scatter(centers[:, 0], centers[:, 1], s=5, c='red', marker='o')

# Відображення точок вихідного датасету чорним кольором з насиченістю 10%
ax.scatter(data[:, 0], data[:, 1], c='black', s=5, alpha=0.1)

# Виведення результатів у файл графічного формату
plt.savefig('output.png')

# Відображення графіки
plt.show()