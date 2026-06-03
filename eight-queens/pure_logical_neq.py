import itertools
import itertools
from kanren import run, var, fact, Relation, conde, eq

#neq函数
def neq(a, b):
    def goal(s):
        a_val = a.value if hasattr(a, 'value') else a
        b_val = b.value if hasattr(b, 'value') else b
        if a_val != b_val:
            yield s
    return goal


def solve_queens():
    q1, q2, q3, q4, q5, q6, q7, q8 = var(), var(), var(), var(), var(), var(), var(), var()
    values = range(8)
    # 使用neq构建约束
    constraints = []
    queens_vars = [q1, q2, q3, q4, q5, q6, q7, q8]
    
    # 确保所有变量是不同的（排列）
    for i in range(8):
        for j in range(i+1, 8):
            constraints.append(neq(queens_vars[i], queens_vars[j]))
    
    #对角线约束
    for i in range(8):
        for j in range(i+1, 8):
            constraints.append(neq(abs(queens_vars[i] - queens_vars[j]), abs(i - j)))
    
    #运行查询
    return run(0, (q1, q2, q3, q4, q5, q6, q7, q8), *constraints,*[eq(q, values) for q in queens_vars])

# 测试
print("使用neq约束方法：")
solutions = solve_queens()
print(f"共有 {len(solutions)} 种有效解")