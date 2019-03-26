def bug_in_apple(apple):
    return [[x, y.index("B")] for x, y in enumerate(apple) if "B" in y][0]


apple = [
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"]
]
if __name__ == '__main__':
    print(bug_in_apple(apple))
