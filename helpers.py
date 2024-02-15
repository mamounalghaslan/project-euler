
# generates the fibonacci sequence up to, but not including, n
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a + b


# checks if a number is prime
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# returns a list of factors of a number
def factors(n):
    factors_ = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors_.append(i)
            factors_.append(n // i)
    return factors_


# returns a list of prime factors of a number
def prime_factors(n):
    factors_ = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors_.append(i)
            n //= i
    if n > 1:
        factors_.append(n)
    return factors_


# checks if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

