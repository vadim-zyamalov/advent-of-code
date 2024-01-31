def extended_gcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1

    while b:
        q, r = divmod(a, b)
        a, b = b, r
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, s0 - q * t1

    return a, s1, t1
