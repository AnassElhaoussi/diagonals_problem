test_cases = int(input())


for _ in range(test_cases):
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])
    diag = n
    diag_count = 0

    while k > diag:
        diag_count += 1
        k -= diag
        if diag_count % 2 != 0:
            diag -= 1
    if k> 0:

        diag_count += 1

    print(diag_count)