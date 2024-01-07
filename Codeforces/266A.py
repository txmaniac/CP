def solve(word):
    count = 0
    for i in range(1, n):
        if word[i] == word[i - 1]:
            count += 1

    return count

if __name__ == "__main__":
    n = int(input())
    word = input()
    print(solve(word))
