def solve(n):
    num = 0
    check = {
        "++X": 1,
        "X++": 1,
        "--X": -1,
        "X--": -1
    }

    while n:
        n -= 1
        key = input()
        num += check[key]

    print(num)
    
if __name__ == "__main__":
    n = int(input())
    solve(n)