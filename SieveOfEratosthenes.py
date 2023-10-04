def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes


n = int(input("Enter the value of n: "))
prime_numbers = sieve_of_eratosthenes(n)
print(f"Prime numbers less than or equal to {n}: {prime_numbers}")

