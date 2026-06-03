以下是为你的八皇后问题实验项目编写的 `README.md`，适合放在 GitHub 仓库中展示。

---

```markdown
# 八皇后问题实验：命令式编程 vs 逻辑编程

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


## 📖 项目简介

本项目以经典的**八皇后问题**为载体，系统对比了**命令式编程**与**逻辑编程**两种编程范式在问题求解中的差异。通过多种算法实现（穷举法、深度优先搜索、逻辑编程），深入分析了各方法的时间复杂度、空间效率及代码可读性。

### 八皇后问题

> 在 8×8 的国际象棋棋盘上放置八个皇后，使得任意两个皇后都不在同一行、同一列或同一对角线上。找出所有满足条件的摆法。

已知共有 **92 种** 有效解。

## 🎯 实验目的

- 理解命令式编程与逻辑编程的核心区别
- 掌握穷举法、DFS回溯算法的实现与复杂度分析
- 学习使用 `kanren` 库进行逻辑编程
- 对比不同方法的时间效率与代码简洁性

## 📁 项目结构

```
eight-queens/
├── generate_all.py          # 穷举法：生成所有排列（40320种）
├── generate_valid.py        # 穷举法：筛选有效解（92种）
├── pure_logical.py          # 逻辑编程：将有效解作为事实导入
├── pure_logical_neq.py      # 逻辑编程：使用neq约束声明式求解
├── neq.py                   # 自定义neq不等约束函数
├── logical_neq.py           # 完整的neq约束求解器
└── generate_out/            # 输出目录
    ├── all_sequences.txt    # 所有排列（40320种）
    └── all_solutions.txt    # 有效解（92种）
DFS/
└── DFS_eight_queens.py      # 深度优先搜索（DFS）回溯法
```

## 🚀 快速开始

### 环境要求

- Python 3.7+
- kanren 库（逻辑编程）

### 安装依赖

```bash
pip install kanren
```

### 运行实验

```bash
# 1. 穷举法：生成所有排列
python generate_all.py

# 2. 穷举法：筛选有效解
python generate_valid.py

# 3. 逻辑编程（事实导入法）
python pure_logical.py

# 4. 逻辑编程（neq约束法）
python pure_logical_neq.py

# 5. DFS回溯法
python DFS_eight_queens.py
```

## 📊 算法对比

| 方法 | 时间复杂度 | 空间复杂度 | 优点 | 缺点 |
|------|-----------|-----------|------|------|
| 穷举法 | O(n! × n²) | O(n!) | 实现简单，逻辑直观 | 效率最低，内存消耗大 |
| 逻辑编程（事实导入） | O(n! × n²) | O(n) | 代码简洁 | 本质仍是命令式，未发挥逻辑编程优势 |
| 逻辑编程（neq约束） | O(n!) | O(n) | 代码最简洁，声明式思维 | 运行效率依赖引擎 |
| DFS回溯 | 远小于 O(n!) | O(n) | 内存效率高，剪枝高效 | 实现稍复杂 |

## 🔬 核心实现

### 1. 穷举法

```python
# 生成 [0,1,2,3,4,5,6,7] 的所有排列
def generate_permutations(nums, start_idx, result):
    if start_idx == len(nums) - 1:
        result.append(nums.copy())
        return
    for i in range(start_idx, len(nums)):
        nums[start_idx], nums[i] = nums[i], nums[start_idx]
        generate_permutations(nums, start_idx + 1, result)
        nums[start_idx], nums[i] = nums[i], nums[start_idx]
```

### 2. DFS回溯法

```python
def place_queen(current_board):
    if len(current_board) == 8:
        all_solutions.append(current_board.copy())
        return
    for column in range(8):
        if is_safe(current_board, column):
            current_board.append(column)
            place_queen(current_board)
            current_board.pop()  # 回溯
```

### 3. 逻辑编程（neq约束）

```python
def neq(a, b):
    def goal(s):
        a_val = a.value if hasattr(a, 'value') else a
        b_val = b.value if hasattr(b, 'value') else b
        if a_val != b_val:
            yield s
    return goal

# 声明约束：所有皇后不在同一列
for i in range(8):
    for j in range(i+1, 8):
        constraints.append(neq(queens_vars[i], queens_vars[j]))
```

## 📈 运行结果示例

```
# 穷举法输出
Results saved to: generate_out/all_sequences.txt
Total solutions: 40320

# 有效解筛选
Results saved to: generate_out/all_solutions.txt
Total solutions: 92

# 逻辑编程输出
共有 92 种有效解

# DFS输出
找到 92 个解决方案
方案1: [0, 4, 7, 5, 2, 6, 1, 3]
方案2: [0, 5, 7, 2, 6, 3, 1, 4]
...
```

## 💡 关键发现

1. **命令式编程**：需要指定每一步的具体操作（如何生成排列、如何检查冲突），关注"怎么做"。

2. **逻辑编程**：只需描述问题的约束规则（皇后不能在同一列、同一对角线），由引擎自动推导解，关注"是什么"。

3. **调试难点**：直接对逻辑变量使用 Python 原生运算符（如 `abs(q1 - q2)`）会导致 `TypeError`，必须将约束封装为延迟执行的 `goal` 函数。

4. **效率对比**：DFS 回溯法通过剪枝大幅减少搜索空间，是实际应用中最优的命令式解法；逻辑编程在代码简洁性上胜出，适合快速原型验证。

## 🔧 可改进方向

- [ ] 实现基于位运算的 DFS（进一步优化效率）
- [ ] 补充 BFS 广度优先搜索版本
- [ ] 扩展到 N 皇后问题（N=10,12,14）
- [ ] 使用 `time` 和 `memory_profiler` 进行性能定量测试
- [ ] 添加对称性剪枝优化

## 📚 参考资料

- [kanren 逻辑编程库文档](https://github.com/pythological/kanren)
- [八皇后问题 - Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)

