def n_primos(n):
    quantidade = 0
    x = 2
    while n >= x:
        while n % x != 0 and x <= n/2:
            x += 1
        if n % x == 0 and n != x:
            n -= 1
        else:
            quantidade += 1
            x = 2
            n -= 1
    return quantidade