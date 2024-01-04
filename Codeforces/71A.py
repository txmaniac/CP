def solve(word):
    print(word if len(word) <= 10 else f'{word[0]}{len(word)-2}{word[-1]}')
    return

if __name__ == "__main__":
    n = int(input())
    while n:
        word = input() 
        solve(word)
        n -= 1