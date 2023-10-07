def simple_sieve(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]  
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    
    return [i for i, prime in enumerate(sieve) if prime]

def segmented_sieve(n):
    delta = int(n**0.5) + 1
    primes = simple_sieve(delta)
    result = list(primes)  
    
    for m in range(delta, n + 1, delta):
        segment = [True] * delta
        lower_limit = m - delta + 1
        
        for prime in primes:
            start = max(prime * prime, (lower_limit + prime - 1) // prime * prime)
            segment_start = start - lower_limit
            segment[segment_start:m-lower_limit+1:prime] = [False] * len(range(segment_start, m-lower_limit+1, prime))
        
        result.extend([i + lower_limit for i, is_prime in enumerate(segment) if is_prime])
                
    return result

if __name__ == "__main__":
    n = int(input("Enter the upper limit n: "))
    print(segmented_sieve(n))



