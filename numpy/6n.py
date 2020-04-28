import numpy as np

# 使用索引数组进行索引
a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])

palette = np.array([[0, 0, 0],                # black
                    [255, 0, 0],              # red
                    [0, 255, 0],              # green
                    [0, 0, 255],              # blue
                    [255, 255, 255]])
image = np.array([[0, 1, 2, 0],           # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])

a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1],                        # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],                        # indices for the second dim
              [3, 3]])
print(a)
print(a[i, j])
print(a[i, 2])
print(a[:, j])

time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5, 4)
print(time)
print(data)

index = data.argmax(axis=0)
print(index)
print(time[index])
data_max = data[index, range(data.shape[1])]
print(data_max)
print(np.all(data_max == data.max(axis=0)))
