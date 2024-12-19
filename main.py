import numpy
import matplotlib.pyplot as plt

def f(x): # traite les array des nombres
    return x**2 - 8 * numpy.log(x)


def solve_equation(f, left,right, precision=10**(-3)) :
    while right - left >= precision:
        middle = (right + left) / 2
        if f(middle) == 0:
            print(middle)
            break
        elif f(left) * f(middle) < 0:
            right = middle
        elif f(right) * f(middle)  <0:
            left = middle
    return middle

def plot_function(f, start, end, step=0.01):
    x = numpy.arange(start, end, step)
    y = f(x)
    plt.figure(figsize=(15, 6))
    plt.plot(x, y)
    plt.show()
    
if __name__ == "__main__":   
   plot_function(f, start=0.01, end=5, step=0.01)
   """  x = numpy.array([1, 2, 3])
    y = f(x)
    middle = silve_equation(f, left=0, right=0)
    print(middle)
    print(f(middle))  
 """

