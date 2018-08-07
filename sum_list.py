from primes import get_primes

def prod_greater_1000(sum):
    primes_list = get_primes(2000)
    sum_feasible = True
    for a in range(1,int(sum/2)+1):
        b = sum - a
        if a in primes_list and b in primes_list and a*b > 1000:
            sum_feasible = False
            break
    return sum_feasible,a,b

def get_sum():
    primes_list = get_primes(2000)
    print(primes_list)
    sum_list = []
    non_sum_list = dict()
    for sum in range(3,2001):
        # is sum = 1 + prime then exclude
        sum_feasible = True
        if sum-1 in primes_list:
            non_sum_list[sum] = [sum-1]
            continue
        # if sum = p1 + p2 st p1xp2 > 1000 then exclude
        sum_feasible,a,b = prod_greater_1000(sum)
        if sum_feasible:
            sum_list.append(sum)
        else:
            non_sum_list[sum] = [a,b]

    return sum_list,non_sum_list

if __name__ == "__main__":
    print(get_sum())
    # print(prod_greater_1000(100)[1])