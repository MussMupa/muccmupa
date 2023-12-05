import matplotlib.pyplot as plt #для иллюстрации графиков
import numpy as np #мат функции
import os #для работы с файлами

if __name__ == '__main__': #основное тело программы
    x = np.linspace(-10,10,1000)
    A = 9.66459
    y = -np.abs(np.sin(x)*np.cos(A)*np.exp(np.abs(1-np.sqrt(x**2+A**2)/np.pi)))
    plt.axis([-10,10,-20,0]) 
    plt.plot(x,y)
    plt.show()#задаем оси графиков, выводим их, показываем

    if 'results' not in os.listdir(): #условие на наличие папки результаты в текущей директории
        os.makedirs(os.path.join(os.getcwd(), 'results')) #создает папку в случае ее отсутствия
    #открывает файл рузультатов и вносит туда полученные значения в формате i+1 x[i] y[i] номер строки, значение x и значение функции y(x)
    with open("results/results.csv", "w", encoding="utf-8") as file: 
        for i in range(len(x)):
            file.write('{}, {}, {}\n'.format(i + 1, x[i], y[i]))
