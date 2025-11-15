import sys
def a():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1)
    except ValueError:
        return
    xor_sum = 0
    line2 = sys.stdin.readline()
    if line2:
        for num_str in line2.split():
            try:
                xor_sum ^= int(num_str)
            except ValueError:
                break
    for i in range(1, n + 1):
        xor_sum ^= i
    print(xor_sum)
a()
