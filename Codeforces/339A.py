def solve(nums):
    if len(nums) > 1:
        counts = [0] * 4

        # count sort O(n)
        for num in nums:
            counts[int(num)] += 1
        
        res = ""
        for i in range(len(counts)):
            while counts[i]:
                res += str(i) + "+"
                counts[i] -= 1

        return res[:-1]
    else:
        return nums[0]
    
if __name__ == "__main__":
    list = input().split("+")
    print(solve(list))