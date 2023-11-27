import matplotlib.pyplot as plt

with open('DS4.txt', 'r') as file:
    data = [tuple(map(int, line.strip().split())) for line in file]

plt.figure(figsize=(960/80, 540/80)) 

x, y = zip(*data)
plt.scatter(x, y)

plt.savefig('result.png')
plt.show()