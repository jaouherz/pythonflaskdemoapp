

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False

    return True


def get_nth_prime(n):
    if n <= 0:
        return -1
    if n == 1:
        return 2

    prime_counter = 1
    current_number = 2

    while prime_counter < n:
        current_number += 1
        is_prime = True

        for i in range(2, int(current_number/2)+1):
            if current_number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_counter += 1

    return current_number
