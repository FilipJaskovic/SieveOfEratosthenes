# SieveOfEratosthenes
 
This repository contains implementations of the classic Sieve of Eratosthenes algorithm and the Segmented Sieve algorithm, both used to find all prime numbers up to a specified integer `n`.

## Description

- **Sieve of Eratosthenes**: An ancient algorithm used to find all primes up to a given value. This implementation provides a straightforward and efficient approach to generate a list of prime numbers.
  
- **Segmented Sieve**: An optimized version of the Sieve of Eratosthenes, which divides the range [0, n] into smaller segments and finds primes in each segment. This method reduces the space complexity and is particularly useful when `n` is large, and we want to find primes in a specific segment without using memory proportional to `n`.
## Usage
For both algorithms:
1. Run the respective script.
2. Enter the desired integer `n` when prompted.
3. The script will output all prime numbers less than or equal to `n`.

## Example

Enter the value of n: 30
Prime numbers less than or equal to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

## Code

### Classic Sieve of Eratosthenes

Here is the main function, `sieve_of_eratosthenes(n)`:

```python
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes
```

### Segmented Sieve

Here are the main functions for the Segmented Sieve:

#### Simple Sieve

```python
def simple_sieve(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]  
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    
    return [i for i, prime in enumerate(sieve) if prime]
```

#### Segmented Sieve
```python
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
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Happy coding!