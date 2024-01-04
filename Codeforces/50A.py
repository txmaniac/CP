def solve(n, k):
    print((n * k)// 2)
    
if __name__ == "__main__":
    n, k = (int(i) for i in input().split())
    solve(n, k)