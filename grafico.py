import time
import matplotlib.pyplot as plt

def crivo(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes

def tempo(n):
    start_time = time.time()
    crivo(n)
    end_time = time.time()
    return end_time - start_time

# Valores de n para teste
n_values = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000]
execution_times = []

for n in n_values:
    exec_time = tempo(n)
    execution_times.append(exec_time)
    print(f"Tempo de execução para n={n}: {exec_time:.6f} segundos")

# Plotar gráfico
plt.plot(n_values, execution_times, marker='o')
plt.xlabel('n')
plt.ylabel('Tempo de execução (segundos)')
plt.title('Tempo de execução')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
