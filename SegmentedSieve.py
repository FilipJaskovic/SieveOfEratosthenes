def simple_sieve(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

def segmented_sieve(n):
    delta = int(n**0.5) + 1
    primes = simple_sieve(delta)
    result = list(primes)
    
    for m in range(delta, n + 1, delta):
        segment = [True] * delta
        lower_limit = m - delta + 1
        
        for prime in primes:
            start = max(prime * prime, (lower_limit // prime + (lower_limit % prime > 0)) * prime)
            for j in range(start, m + 1, prime):
                segment[j - lower_limit] = False
        
        for i, is_prime in enumerate(segment):
            if is_prime and i + lower_limit <= n:
                result.append(i + lower_limit)
                
    return result

n = int(input("Enter the upper limit n: "))
print(segmented_sieve(n))

