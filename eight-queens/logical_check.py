import itertools

def check_diagonals(seq):
    for i in range(8):
        for j in range(i+1, 8):
            if abs(i - j) == abs(seq[i] - seq[j]):
                return False
    return True

# 8个不同数字0~7的全排列
all_perms = list(itertools.permutations(range(8), 8))

your_solution = (4, 0, 5, 7, 2, 6, 1, 3)  

if your_solution in all_perms and check_diagonals(your_solution):
    print(f"解 {your_solution} 是有效解")
else:
    print(f"解 {your_solution} 不是有效解")