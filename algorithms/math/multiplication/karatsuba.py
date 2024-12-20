def karatsuba(x: int, y: int):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half_n = n // 2

    a = x // (10**half_n)
    b = x % (10**half_n)
    c = y // (10**half_n)
    d = y % (10**half_n)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)

    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    return (ac * (10 ** (2 * half_n))) + (ad_plus_bc * (10**half_n)) + bd


def main():
    x = 500_000_000_000

    print(karatsuba(x, x))


if __name__ == "__main__":
    main()
