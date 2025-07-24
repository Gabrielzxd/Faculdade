class Solution(object):
    def calPoints(self, operations):
        ops = []
        for op in operations:
            if op == 'C':
                ops.pop()
            elif op == 'D':
                ops.append(2 * ops[-1])
            elif op == '+':
                ops.append(ops[-1] + ops[-2])
            else:
                ops.append(int(op))
        return sum(ops)
