def solve(k):
    count = 0
    nums = [int(i) for i in input().split()]
    thres = nums[k-1]
    for num in nums:
        count += int(num >= thres and num != 0)
    
    print(count)

if __name__ == "__main__":
    n, k = (int(i) for i in input().split())
    solve(k)