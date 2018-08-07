from primes import get_prime_factors
from primes import get_primes
from partition import get_partitions
from functools import reduce

def get_prod_list():
    primes = get_primes(1000)
    possible_prod_dict = dict()
    non_prod_dict = dict()
    for a in range(1,10):
        for b in range(a,10):
            prod = a*b
            if a*b == 1:
                possible_prod_dict[1] = {(1,1)}
                continue
            prime_factor_list = get_prime_factors(primes,prod)
            partition_list = get_partitions(prime_factor_list)
            possible_factors = set()
            for (x,y) in partition_list:
                num1 = reduce(lambda u, v: u * v, x, 1)
                num2 = reduce(lambda u, v: u * v, y, 1)
                if num2>=num1:
                    temp_pair = (num1, num2)
                else:
                    temp_pair = (num2, num1)
                # print(num1,num2)
                possible_factors.add(temp_pair)
            possible_prod_dict[a*b] = possible_factors
            # print(possible_prod_dict)
            # assert False
    return possible_prod_dict


if __name__ == "__main__":
    print(get_prod_list())