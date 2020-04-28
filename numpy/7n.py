import numpy as np
import matplotlib.pyplot as plt

# a = np.arange(12).reshape(3, 4)
# print(a)
# b = a > 4
# print(b)
# print(a[b])
# a[b] = 0
# print(a)


def mandelbrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape,dtype=int)
    for i in range(maxit):
        z = z**2  +c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2      
    return divtime

plt.imshow(mandelbrot(400,400))
plt.show()
