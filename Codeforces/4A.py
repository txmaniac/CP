def solve(x):
    if x % 2 or x == 2: return "NO"
    for i in range(2, x // 2, 2):
        if i % 2 or (x - i) % 2:
            return "NO"
        
    return "YES"

if __name__ == "__main__":
    x = int(input())
    print(solve(x))