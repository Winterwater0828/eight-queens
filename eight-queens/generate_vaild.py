import os

# 创建结果保存目录
result_dir = "generate_out"
os.makedirs(result_dir, exist_ok=True)

def is_valid(list):
    n = len(list)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(list[i] - list[j]) == abs(i - j):
                return False
    return True

# 生成全排列：
def generate_permutations(nums, start_idx, result):
    if start_idx == len(nums) - 1:
        result.append(nums.copy())
        return
    for i in range(start_idx, len(nums)):
        nums[start_idx], nums[i] = nums[i], nums[start_idx]
        generate_permutations(nums, start_idx + 1, result)
        nums[start_idx], nums[i] = nums[i], nums[start_idx]

# 穷举出符合约束的所有排列：
def solutions(numbers):
    all_solutions = []
    all_permutations = []
    generate_permutations(numbers, 0, all_permutations)
    for permutation in all_permutations:
        if is_valid(permutation):
            all_solutions.append(permutation)
    return all_solutions

# 获取结果并保存
if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    results = solutions(nums)
    # 保存结果到文件
    output_file = os.path.join(result_dir, "all_solutions.txt")
    with open(output_file, "w") as f:
        for idx, solution in enumerate(results, 1):
            f.write(f"{solution}\n")
    
    print(f"Results saved to: {output_file}")
    print(f"Total solutions: {len(results)}")