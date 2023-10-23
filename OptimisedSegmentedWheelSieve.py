def segmented_sieve_with_wheel(n):
    if n < 2:
        return []

    # Directly set base primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n < 30:
        return [prime for prime in primes if prime <= n]

    # Direct memory allocation to avoid overhead
    limit = int(n ** 0.5) + 1
    sieve_limit = [1] * limit
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve_limit[i]:
            sieve_limit[i * i::i] = [0] * len(sieve_limit[i * i::i])

    # Inline wheel for primes up to sqrt(n)
    WHEEL_INDICES = [31, 37, 41, 43, 47, 49, 53, 59]
    WHEEL_NEXT = [6, 4, 2, 4, 2, 4, 6, 2]

    p = 31
    p_idx = 0
    while p * p <= n:
        if sieve_limit[p]:
            sieve_limit[p * p::p] = [0] * len(sieve_limit[p * p::p])
        p += WHEEL_NEXT[p_idx]
        p_idx = (p_idx + 1) % 8  # Wrapping around the index

    primes += [i for i, is_prime in enumerate(sieve_limit) if is_prime]

    # Direct memory allocation for segments
    segment_size = 2 * limit
    for low in range(limit, n + 1, segment_size):
        sieve_length = min(segment_size, n - low + 1)
        sieve = [1] * sieve_length
        high = min(n, low + sieve_length - 1)

        for prime in primes:
            if prime == 0:
                continue
            sieve[max(prime * prime, (low + prime - 1) // prime * prime) - low: high + 1: prime] = [0] * len(sieve[max(prime * prime, (low + prime - 1) // prime * prime) - low: high + 1: prime])
        
        # Inline wheel for sieved segments
        for i in range(7, sieve_length, 2):
            if sieve[i]:
                primes.append(i + low)

    return primes

if __name__ == "__main__":
    n = int(input("Enter the upper limit n: "))
    print(segmented_sieve_with_wheel(n))
