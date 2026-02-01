

_count = 0

while True:
    _divider = int(input("Enter a divider: "))
    _num = int(input("Enter a number: "))
    if _divider > _num:
        print("Divider is greater than number, please try again")
        continue
    for i in range(_num, 1 , -_divider):
        _count += 1
    print(_count)
