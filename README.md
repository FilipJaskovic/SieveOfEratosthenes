# SieveOfEratosthenes
 
This repository contains an implementation of the Sieve of Eratosthenes algorithm, which is used to find all prime numbers up to a specified integer `n`.

## Description

The Sieve of Eratosthenes is an ancient algorithm used to find all primes up to a given value. This implementation provides a straightforward and efficient approach to generate a list of prime numbers.

## Usage

1. Run the script.
2. Enter the desired integer `n` when prompted.
3. The script will output all prime numbers less than or equal to `n`.

## Example

Enter the value of n: 30
Prime numbers less than or equal to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

## Code

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
Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Happy coding!