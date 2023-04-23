# this code is to study regression patterns on frequency curve

# function that returns all primes' powers list up until given number

import pandas as pd

data = pd.read_csv("1m.csv")

prime_list = data['Num']

totnoofprimes = len(prime_list)


# this function returns 2D prime power list

def two_d_list(upper_lim):
    total_no_of_primes = totnoofprimes
    k = 0
    prime_list_new = []
    while (prime_list[k] <= upper_lim) and (k <= total_no_of_primes):
        prime_list_new.append(prime_list[k])
        k += 1

    l2 = []
    for prime in prime_list_new:

        l1 = [0]

        power = prime
        while power <= upper_lim:
            l1.append(power)
            power *= prime

        l2.append(l1)

    return l2


def single_rep_diff_finder(target):
    # Finding difference creating prime.
    # And returning both the difference creating prime and the difference

    # we will create difference using a prime in range target-100 and target-7

    for i in range(totnoofprimes):
        if prime_list[i] > target - 100:
            break

    differentiating_prime = prime_list[i]

    difference = target - differentiating_prime

    return [target, difference, differentiating_prime]


def differences_list_maker_range(range_low_lim, range_upper_lim):
    # Return a list of differences and the differentiating primes used for a range of numbers.
    # Store of them in one giant 2D list
    # The lists for each number in the list would be:
    # [ Current number in range ( target number ), difference, differentiating prime]

    return_list = []

    for j in range(range_low_lim, range_upper_lim):
        list1 = single_rep_diff_finder(j)
        return_list.append(list1)

    return return_list


l = differences_list_maker_range(200, 250)

file1 = open("MyFile4.txt", "w")

for internal_list in l:
    for internal_list_term in internal_list:

        file1.write(f"{internal_list_term}\t")
    file1.write(f"\n")

file1.close()
print("Done")
