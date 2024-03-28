import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def main():
    max_number = 10000
    x = []
    y = []
    for i in range(1, max_number + 1):
        iterations = collatz(i)
        x.append(iterations)  # Número de iteraciones
        y.append(i)           # Número de inicio de la secuencia

    plt.scatter(x, y, s=5)  # s es el tamaño de los puntos en el gráfico
    plt.title('Número de Collatz')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número de inicio de la secuencia')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
