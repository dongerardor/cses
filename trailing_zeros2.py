def solve(N):
    if N == 0:
        return 0

    return N // 5 + solve(N // 5)

num = int(input())
print(solve(num))
