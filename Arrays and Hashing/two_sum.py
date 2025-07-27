def two_sum(nums, target):
    num_map = {}  # value → index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return []

# ------------------------------
def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Indices:", result)  # Output: [0, 1]

if __name__ == "__main__":
    main()
