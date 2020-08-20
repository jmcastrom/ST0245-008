def tarjeta(n):
    if n <= 1:
        return 1
    else:
        print(n, end=" ")
        return tarjeta(n-1)
print(tarjeta(63))