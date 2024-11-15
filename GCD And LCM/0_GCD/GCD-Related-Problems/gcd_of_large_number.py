def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        a = int(a)

        if a == 0:
            print(b)
            continue

        b_mod_a = 0
        for digit in b:
            b_mod_a = (b_mod_a * 10 + int(digit)) % a

        print(gcd(a, b_mod_a))


if __name__ == "__main__":
    main()
