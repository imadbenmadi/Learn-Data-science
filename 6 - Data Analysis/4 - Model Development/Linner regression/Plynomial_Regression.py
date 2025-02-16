import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import clean data
df = {"price" : [13495, 16500, 16500, 13950, 17450, 15250, 17710, 18920, 23875, 17859],
      "horsepower" : [111, 154, 102, 115, 110, 110, 110, 140, 160, 101],
                  "highway-mpg" : [27, 22, 24, 25, 20, 29, 27, 25, 20, 29]}
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()
x = df['highway-mpg']
y = df['price']
f = np.polyfit(x, y, 10)
p = np.poly1d(f)
print(p)
PlotPolly(p, x, y, 'highway-mpg')



# create 11 order polynomial model with the variables x and y from above
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
print(p1)