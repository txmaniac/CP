def solve(n):
    count = 0
    while n:
        nums = [int(item) for item in input().split(" ")]
        count += int(sum(nums) >= 2)
        n -= 1
    print(count)
    

if __name__ == "__main__":
    n = int(input())
    solve(n)