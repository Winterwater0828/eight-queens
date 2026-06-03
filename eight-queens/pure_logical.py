import itertools
from kanren import run, var, fact, Relation

#建立一个空的关系表
valid_board=Relation()

#判断满足对角线约束
def check_diagonals(list):
    for i in range(8):
        for j in range(i+1,8):
            if abs(i-j)==abs(list[i]-list[j]):
                return False
    return True

#穷举法生成所有8!种排列
all_perms=list(itertools.permutations(range(8)))

#筛选有效解
valid_perms=[p for p in all_perms if check_diagonals(p)]

#逻辑筛选
for p in valid_perms:
    fact(valid_board,p)

#查询结果
x=var()
solutions=run(0,x,valid_board(x))
print(f"共有 {len(solutions)} 种有效解")