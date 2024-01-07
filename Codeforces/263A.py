def solve(coords):
    return abs(coords[0] - 2) + abs(coords[1] - 2)
    
if __name__ == "__main__":
    for i in range(5):
        row = input().split(" ")
        if "1" in row:
            coords = (i, row.index("1"))
            
    print(solve(coords))