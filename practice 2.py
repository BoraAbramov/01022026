
while True:
    _low = int(input("Enter a number: "))
    _high = int(input("Enter a number: "))
    if _high <= _low:
        continue
    else:
        for i in range(_high, _low, -1):
            print(i, end=" ")