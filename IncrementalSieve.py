def incremental_sieve():
    # Yield the first two primes
    yield 2
    yield 3

    found_primes = [2, 3]  # List of discovered primes
    composites = {}  # Dict: keys are non-prime numbers, values are steps (increments) associated with each prime

    candidate = 5  # Start with the first odd number after 3
    while True:
        if candidate not in composites:
            yield candidate
            found_primes.append(candidate)
            # Square of the prime number is the first composite number that's uniquely identified by this prime.
            composites[candidate * candidate] = 2 * candidate
        else:
            step = composites.pop(candidate)
            next_composite = candidate + step
            while next_composite in composites:
                next_composite += step
            composites[next_composite] = step

        # Move to the next odd number
        candidate += 2

# Test the sieve generator
# gen = incremental_sieve()
# for _ in range():
#     print(next(gen))
gen = incremental_sieve()
try:
    while True:
        print(next(gen))
except KeyboardInterrupt:
    print("\nGenerator stopped by user.")
