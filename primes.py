def get_prime_factors(primes_list,x):
    factors = []
    for div in primes_list:
        if div > x:
            break
        if x%div == 0:
            while (x%div==0):
                x = x/div
                factors.append(div)
    return factors

def get_primes(n):
    primes = [2]
    for n in range(2,n+1):
        is_prime = True
        for divisor in primes:
            if n%divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

if __name__ == "__main__":
    primes_list = get_primes(100)
    print(primes_list)

    print(get_prime_factors(primes_list,123))