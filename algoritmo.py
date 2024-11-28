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

# entrada do valor de n
n = int(input("Digite um número inteiro: "))

# Listar os números primos menores ou iguais a n
primes = crivo(n)
print(f"Números primos menores ou iguais a {n}:")
print(primes)
