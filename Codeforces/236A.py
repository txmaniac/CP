def solve(x):
    return "IGNORE HIM!" if len(set(x)) % 2 else "CHAT WITH HER!" 

if __name__ == "__main__":
    x = input()
    print(solve(x))