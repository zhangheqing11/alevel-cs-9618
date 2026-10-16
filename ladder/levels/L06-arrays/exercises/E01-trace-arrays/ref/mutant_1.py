# M1: intentional fault from spec.md.
PREDICTED = ["4 25", "0 1 16", "4 99", "23 12"]


def run_trace() -> None:
    nums = [0] * 5  # ARRAY[1:5] OF INTEGER
    for index in range(1, 6):
        nums[index - 1] = index * index
    print(nums[1], nums[4])
    for index in range(4, 0, -1):
        nums[index] = nums[index - 1]
    nums[0] = 0
    print(nums[0], nums[1], nums[4])
    copy = nums
    nums[2] = 99
    print(copy[2], nums[2])
    grid = [[0] * 3 for _ in range(2)]  # ARRAY[1:2,1:3] OF INTEGER
    for row in range(1, 3):
        for column in range(1, 4):
            grid[row - 1][column - 1] = row * 10 + column
    print(grid[1][2], grid[0][1])


if __name__ == "__main__":
    run_trace()
