def solve(x,y):
    count = 0
    while x <= y:
        x /= 2
        y /= 3
        count += 1

    return count

if __name__ == "__main__":
    (x,y) = (int(i) for i in input().split(" "))
    print(solve(x,y))