def solve():
    x = input().lower()
    y = input().lower()

    if x > y:
        return 1
    elif x < y:
        return -1
    
    return 0

if __name__ == "__main__":
    print(solve())