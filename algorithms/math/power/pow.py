def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n == 1:
        return x

    # If exponent is negative then calculate: 1 / x ^ abs(n)
    if n < 0:
        return 1 / (my_pow(x, abs(n)))

    # If the exponent is even, then calculate x ^ (n // 2) and multiply the result with itself to get x ^ n
    if n % 2 == 0:
        x_raise_half_n = my_pow(x, n // 2)
        return x_raise_half_n * x_raise_half_n

    # If the exponent is odd, then subtract 1 from it to make it even.
    # To calculate x ^ n, multiply x ^ (n - 1) with x
    return x * my_pow(x, n - 1)


def main():
    print(my_pow(2.000000, 10))


if __name__ == "__main__":
    main()
