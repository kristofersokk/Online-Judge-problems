

def cycle(a):
    result = 1
    while a != 1:
        a = a / 2 if a % 2 == 0 else 3 * a + 1
        result += 1
    return result


while True:
    (i, j) = input().split()
    print(f"{i} {j} {str(max(cycle(a) for a in range(int(i), int(j) + 1)))}")
