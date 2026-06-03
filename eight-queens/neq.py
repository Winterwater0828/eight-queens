def neq(a, b):
    def goal(s):
        a_val = a.value if hasattr(a, 'value') else a
        b_val = b.value if hasattr(b, 'value') else b
        if a_val != b_val:
            yield s
    return goal

