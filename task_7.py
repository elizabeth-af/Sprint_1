def digit_root(num):
    root = 0
    while num != 0:
        root += num % 10
        num //= 10
        if num // 10 == 0 and root > 9:
            num = root + num % 10
            root = 0

    return root

print(digit_root(889987))
